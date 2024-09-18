from django.utils.translation import gettext_lazy as _

# 401
INVALID_REFRESH_TOKEN = 401_00
INVALID_ACCESS_TOKEN = 401_01
INVALID_TOKEN = 401_02
# 404
USER_NOT_FOUND = 404_00
BOOK_NOT_FOUND = 404_01
BOOK_REVIEW_NOT_FOUND = 404_02
SUGGEST_BOOKS_NOT_FOUND = 404_03
# 409
USER_CONFLICT = 409_00
BOOK_REVIEW_CONFLICT = 409_01
# 500
INTERNAL_SERVER_ERROR = 500_00


ERROR_TRANSLATION = {
    # 401
    INVALID_REFRESH_TOKEN: _("Invalid refresh token"),
    INVALID_ACCESS_TOKEN: _("Invalid access token"),
    INVALID_TOKEN: _("Invalid token"),
    # 404
    USER_NOT_FOUND: _("User does not exists"),
    BOOK_NOT_FOUND: _("Book not found"),
    BOOK_REVIEW_NOT_FOUND: _("Book review not found"),
    SUGGEST_BOOKS_NOT_FOUND: _("there is not enough data about you"),
    # 409
    USER_CONFLICT: _("This user already exists"),
    BOOK_REVIEW_CONFLICT: _("This book review already exists"),
    # 500
    INTERNAL_SERVER_ERROR: _("unexpected error"),
}

