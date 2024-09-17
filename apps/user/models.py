from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from .manager import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=64,
        unique=True,
        help_text=_(
            "Required. 64 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    is_admin = models.BooleanField(default=False, verbose_name=_("is admin"))

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.id} - {self.username}"

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
