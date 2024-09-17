class UserAuthEnum:
    ACCESS_TOKEN = 1
    REFRESH_TOKEN = 2

    TOKEN_TYPE_CHOICES = (
        (ACCESS_TOKEN, "access token"),
        (REFRESH_TOKEN, "refresh token")
    )
