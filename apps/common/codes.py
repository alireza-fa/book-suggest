from django.utils.translation import gettext_lazy as _


INTERNAL_SERVER_ERROR = 500_00
USER_NOT_FOUND = 404_00
USER_CONFLICT = 409_00


ERROR_TRANSLATION = {
    INTERNAL_SERVER_ERROR: _("unexpected error"),
    USER_NOT_FOUND: _("User does not exists"),
    USER_CONFLICT: _("This user already exists"),
}
