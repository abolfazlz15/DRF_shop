from rest_framework import viewsets

from apps.product.models import Category
from apps.product.serializers.admin import CreateCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer