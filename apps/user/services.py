from functools import cache
from abc import ABC, abstractmethod
from typing import Dict

from apps.common import codes
from apps.authentication.services import get_authentication_service
from pkg.rich_error.error import RichError
from apps.user.repositories import get_user_repository


class TokenGenerator(ABC):

    @abstractmethod
    def generate_token(self, user) -> Dict:
        pass


class Repository(ABC):

    @abstractmethod
    def check_user_is_exist_by_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def get_user_by_user_name(self, username: str):
        pass

    @abstractmethod
    def register_user(self, username: str, password: str):
        pass


class UserService:
    Op = "user.services.UserService."

    def __init__(self, repo: Repository, token_generator: TokenGenerator):
        self.repo = repo
        self.token_generator = token_generator

    def login(self, username: str, password: str):
        op = self.Op + "login"
        meta = {"username": username}

        if not self.repo.check_user_is_exist_by_username(username=username):
            raise RichError(op).set_code(codes.USER_NOT_FOUND).set_meta(meta)

        user = self.repo.get_user_by_user_name(username=username)
        if not user.check_password(password):
            raise RichError(op).set_code(codes.USER_NOT_FOUND).set_meta(meta)

        return {
            "token": self.token_generator.generate_token(user=user),
            "user": user,
        }

    def register(self, username: str, password: str):
        op = self.Op + "register"

        if self.repo.check_user_is_exist_by_username(username=username):
            raise RichError(op).set_code(codes.USER_CONFLICT)

        user = self.repo.register_user(username=username, password=password)

        return {
            "token": self.token_generator.generate_token(user=user),
            "user": user
        }


@cache
def get_user_service():
    return UserService(
        repo=get_user_repository(),
        token_generator=get_authentication_service()
    )
