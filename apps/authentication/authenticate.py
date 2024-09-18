from typing import Optional, Tuple

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework.request import Request

from rest_framework_simplejwt.authentication import AuthUser
from rest_framework_simplejwt.authentication import JWTAuthentication as BaseJWTAuthentication
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.exceptions import InvalidToken

from .services import get_authentication_service


User = get_user_model()
service = get_authentication_service()


class JWTAuthentication(BaseJWTAuthentication):

    def authenticate(self, request: Request) -> Optional[Tuple[AuthUser, Token]]:
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        try:
            validated_token = service.validate_token(request=request, raw_token=raw_token.decode())
        except Exception:
            raise InvalidToken(
                        {
                            "detail": _("Given token not valid for any token type"),
                        }
                    )

        return self.get_user(validated_token), validated_token
