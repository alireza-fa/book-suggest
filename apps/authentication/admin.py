from django.contrib import admin

from .models import UserAuth


@admin.register(UserAuth)
class UserAuthAdmin(admin.ModelAdmin):
    pass
