from django.urls import path, include

from apps.authentication.views import TokenVerifyView, TokenRefreshView, TokenBanView

app_name = "authentication"

urlpatterns = [
    path("token/", include(([
        path("verify/", TokenVerifyView.as_view(), name="token-verify"),
        path("refresh/", TokenRefreshView.as_view(), name="token-refresh"),
        path("ban/", TokenBanView.as_view(), name="token-ban"),
    ])))
]
