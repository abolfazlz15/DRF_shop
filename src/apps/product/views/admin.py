from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from apps.product.models import Category
from apps.product.serializers.admin import CreateCategorySerializer, CategoryListSerializer, CategoryDetailSerializer, \
    CategoryUpdateOrDeleteSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return CategoryListSerializer
            case 'create':
                return CreateCategorySerializer
            case 'retrieve':
                return CategoryDetailSerializer
            case 'update':
                return CategoryUpdateOrDeleteSerializer
            case 'partial_update':
                return CategoryUpdateOrDeleteSerializer
            case 'destroy':
                return CategoryUpdateOrDeleteSerializer
            case _:
                raise NotAcceptable()
