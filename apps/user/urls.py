from django.urls import path

from apps.user.views import UserLoginView, UserRegisterView, UserInfoView

app_name = "user"

urlpatterns = [
    path("login", UserLoginView.as_view(), name="usr-login"),
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("info/", UserInfoView.as_view(), name="user-info"),
]
