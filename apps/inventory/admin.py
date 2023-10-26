from django.contrib import admin

from apps.inventory.models import StockRecord


@admin.register(StockRecord)
class StockRecordAdmin(admin.ModelAdmin):
    list_display = ['product']
    search_fields = ['product']
