from django.contrib import admin

from auths.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'full_name', 'is_active', 'is_admin', 'is_superuser']
    # list_filter = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    