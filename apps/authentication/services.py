from dataclasses import dataclass
from functools import cache
from abc import ABC, abstractmethod
from typing import Dict

from django.contrib.auth import get_user_model
from django.core.cache import cache as django_cache
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import UserAuth
from authentication.repositories import get_authentication_repository


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

    @abstractmethod
    def create_user_auth(self, user_id: int) -> Model:
        pass


class AuthenticationService:
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
                key=self._get_user_auth_cache_key(user_id=user.id),
                value=user_auth, timeout=self.config.user_auth_cache_exp_in_seconds)

        return user_auth

    def generate_token(self, user: User) -> Dict:
        user_auth = self.get_user_auth(user_id=user.id)

        refresh = RefreshToken.for_user(user=user)
        access = refresh.access_token

        refresh["uuid"] = user_auth.refresh_uuid
        access["uuid"] = user_auth.access_uuid

        return {
            "refresh_token": str(refresh),
            "access_token": str(access)
        }


@cache
def get_authentication_service():
    return AuthenticationService(
        config=Config(),
        repo=get_authentication_repository(),
    )
