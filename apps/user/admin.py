from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'is_active', 'is_admin', 'is_superuser')
    list_filter = ('is_active', 'is_admin', 'is_superuser')
    readonly_fields = ('last_login',)

    fieldsets = (
        (None, {"fields": (
            'username', 'password'
        )}),
        ('permissions', {"fields": (
            'is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions',
        )})
    )

    add_fieldsets = (
        (None, {"fields": (
            'username', 'password1', 'password2'
        )}),
    )

    search_fields = ('username',)
    ordering = ('-id',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            superuser_field = form.base_fields.get('is_superuser')
            if superuser_field:
                superuser_field.disabled = True
            admin_field = form.base_fields.get('is_admin')
            if admin_field:
                admin_field.disabled = True
        return form


admin.site.register(User, UserAdmin)
