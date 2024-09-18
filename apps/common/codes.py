from django.utils.translation import gettext_lazy as _

# 401
INVALID_REFRESH_TOKEN = 401_00
INVALID_ACCESS_TOKEN = 401_01
INVALID_TOKEN = 401_02
# 404
USER_NOT_FOUND = 404_00
# 409
USER_CONFLICT = 409_00
# 500
INTERNAL_SERVER_ERROR = 500_00


ERROR_TRANSLATION = {
    # 401
    INVALID_REFRESH_TOKEN: _("Invalid refresh token"),
    INVALID_ACCESS_TOKEN: _("Invalid access token"),
    INVALID_TOKEN: _("Invalid token"),
    # 404
    USER_NOT_FOUND: _("User does not exists"),
    # 409
    USER_CONFLICT: _("This user already exists"),
    # 500
    INTERNAL_SERVER_ERROR: _("unexpected error"),
}

