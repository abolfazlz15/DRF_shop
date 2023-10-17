from django.contrib import admin
from django.db.models import Count
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from apps.product.models import Category, Product, Option, OptionGroup, ProductAttribute


class ProductAttributeInline(admin.StackedInline):
    model = ProductAttribute
    extra = 2


class AttributeCountFilter(admin.SimpleListFilter):
    """
    show filter by attribute count in product admin
    """
    title = 'Attribute Count'
    parameter_name = 'attr_count'

    def lookups(self, request, model_admin):
        return [
            ('more_5', 'More Than 5'),
            ('lower_5', 'lower Than 5'),
        ]

    def queryset(self, request, queryset):
        if self.value() == "more_5":
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__gt=5)
        if self.value() == "lower_5":
            return queryset.annotate(attr_count=Count('attributes')).filter(attr_count__lte=5)


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'is_shipping', 'track_stock']
    inlines = [ProductAttributeInline]
    list_filter = ['is_active', 'is_shipping', 'track_stock', AttributeCountFilter]
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['enable_is_active', 'disable_is_active']
    def enable_is_active(self, request, queryset):
        queryset.update(is_active=True)

    def disable_is_active(self, request, queryset):
        queryset.update(is_active=False)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Option)
admin.site.register(OptionGroup)
