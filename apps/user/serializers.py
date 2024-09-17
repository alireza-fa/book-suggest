from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

User = get_user_model()


class UserAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=64, validators=[UnicodeUsernameValidator()])

    class Meta:
        model = User
        fields = ("username", "password")


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username",)
