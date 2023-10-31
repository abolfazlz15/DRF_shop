from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from auths.accounts.models import User
from auths.forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone', 'email', 'full_name', 'is_admin')
    list_filter = ('is_admin', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('email', 'full_name', 'profile_image')}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'phone', 'full_name')
    ordering = ('full_name',)
    list_display_links = ('phone', 'email', 'full_name', 'is_admin')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
