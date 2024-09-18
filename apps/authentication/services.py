from dataclasses import dataclass
from functools import cache
from abc import ABC, abstractmethod
from typing import Dict

from django.contrib.auth import get_user_model
from django.core.cache import cache as django_cache
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken, Token

from apps.authentication.models import UserAuth
from apps.authentication.repositories import get_authentication_repository
from common import codes
from pkg.rich_error.error import RichError


@dataclass
class Config:
    prefix_user_auth_cache_key: str = "userauth"
    user_auth_cache_exp_in_seconds: int = 86400  # one day


class Repository(ABC):
    Model = UserAuth

    @abstractmethod
    def check_user_auth_is_exist(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_auth_by_user_id(self, user_id: int) -> Model:
        pass

    @abstractmethod
    def create_user_auth(self, user_id: int) -> Model:
        pass


class AuthenticationService:
    Op = "authentication.services.AuthenticationService."
    User = get_user_model()
    Model = UserAuth

    def __init__(self, config: Config, repo: Repository):
        self.config = config
        self.repo = repo

    def _get_user_auth_cache_key(self, user_id: int) -> str:
        return f"{self.config.prefix_user_auth_cache_key}:{user_id}"

    def get_user_auth(self, user_id: int) -> Model:
        user_auth = django_cache.get(key=self._get_user_auth_cache_key(user_id=user_id))
        if not user_auth:
            if not self.repo.check_user_auth_is_exist(user_id=user_id):
                user_auth = self.repo.create_user_auth(user_id=user_id)
            else:
                user_auth = self.repo.get_user_auth_by_user_id(user_id=user_id)
            django_cache.set(
                key=self._get_user_auth_cache_key(user_id=user_id),
                value=user_auth, timeout=self.config.user_auth_cache_exp_in_seconds)

        return user_auth

    def generate_token(self, user: User) -> Dict:
        user_auth = self.get_user_auth(user_id=user.id)

        refresh = RefreshToken.for_user(user=user)
        access = refresh.access_token

        # we can put ip address or device name for validation and improve security
        refresh["uuid"] = str(user_auth.refresh_uuid)
        access["uuid"] = str(user_auth.access_uuid)

        return {
            "refresh_token": str(refresh),
            "access_token": str(access)
        }

    def _validate_refresh_token(self, token: Token):
        op = self.Op + "_validate_refresh_token"

        user_auth = self.get_user_auth(user_id=token["user_id"])
        if str(user_auth.refresh_uuid) != token["uuid"]:
            raise RichError(op).set_code(codes.INVALID_REFRESH_TOKEN)

    def _validate_access_token(self, token: Token):
        op = self.Op + "_validate_access_token"

        user_auth = self.get_user_auth(user_id=token["user_id"])
        if str(user_auth.access_uuid) != token["uuid"]:
            raise RichError(op).set_code(codes.INVALID_ACCESS_TOKEN)

    def validate_token(self, token_str: str) -> Token:
        op = self.Op + "validate_token"

        try:
            token = UntypedToken(token=token_str)
        except Exception as err:
            raise RichError(op).set_error(err).set_code(codes.INVALID_TOKEN)

        if token["token_type"] == "refresh":
            self._validate_refresh_token(token=token)
        elif token["token_type"] == "access":
            self._validate_access_token(token=token)

        return token

    def refresh_access_token(self, refresh_token_str: str) -> str:
        op = self.Op + "refresh_access_token"

        token = self.validate_token(token_str=refresh_token_str)
        if token["token_type"] != "refresh":
            raise RichError(op).set_msg("token type is not refresh token").set_code(codes.INVALID_REFRESH_TOKEN)

        user_auth = self.get_user_auth(user_id=token["user_id"])

        refresh = RefreshToken(token=str(token))
        access = refresh.access_token
        access["uuid"] = str(user_auth.access_uuid)

        return str(access)

    def ban_token(self, user_id: int) -> None:
        pass


@cache
def get_authentication_service():
    return AuthenticationService(
        config=Config(),
        repo=get_authentication_repository(),
    )
