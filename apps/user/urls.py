from django.urls import path

from user.views import UserLoginView, UserRegisterView

app_name = "user"

urlpatterns = [
    path("login", UserLoginView.as_view(), name="usr-login"),
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("info/", UserInfoView.as_view(), name="user-info"),
]
