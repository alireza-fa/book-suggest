from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.enums.user_auth import UserAuthEnum


class UserAuth(BaseModel):
    user_id = models.PositiveBigIntegerField(verbose_name=_("user id"), db_index=True)
    token_type = models.PositiveSmallIntegerField(choices=UserAuthEnum.TOKEN_TYPE_CHOICES, verbose_name=_("token type"))
    uuid = models.UUIDField(verbose_name=_("uuid"), unique=True, db_index=True)

    class Meta:
        verbose_name = _("UserAuth")
        verbose_name_plural = _("UserAuths")
        ordering = ("-id",)
        unique_together = (["user_id", "token_type"])

    def __str__(self):
        return f"user id: {self.user_id} - token type(a = 1, r = 2): {self.token_type} - {self.uuid}"
