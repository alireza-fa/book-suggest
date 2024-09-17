from django.contrib.auth.models import BaseUserManager as BaseManager


class UserManager(BaseManager):

    def create_user(self, username: str, password: str, is_admin: bool = False, is_superuser: bool = False) -> object:
        if not username:
            raise ValueError("Users must have an fullname")
        if not password:
            raise ValueError("Users must have an national_code")

        user = self.model(
            username=username,
            is_admin=is_admin,
            is_superuser=is_superuser
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)

        return user

    def create_admin(self, username: str, password: str) -> object:
        user = self.create_user(
            username=username,
            password=password,
            is_admin=True,
        )

        return user

    def create_superuser(self, username: str, password: str) -> object:
        user = self.create_user(
            username=username,
            is_admin=True,
            is_superuser=True,
            password=password,
        )

        return user
