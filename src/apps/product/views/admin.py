from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable

from apps.product.models import Category, ProductClass
from apps.product.serializers import admin


class CategoryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Category.objects.filter(depth=1)
        else:
            return Category.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return admin.CategoryListSerializer
            case 'create':
                return admin.CreateCategorySerializer
            case 'retrieve':
                return admin.CategoryDetailSerializer
            case 'update':
                return admin.CategoryUpdateOrDeleteSerializer
            case 'partial_update':
                return admin.CategoryUpdateOrDeleteSerializer
            case 'destroy':
                return admin.CategoryUpdateOrDeleteSerializer
            case _:
                raise NotAcceptable()
            

class ProductClassViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = ProductClass.objects.all()
        return queryset
    
    def get_serializer_class(self):
        match self.action:
            case 'list':
                return admin.ProductClassListSerializer
            case 'retrieve':
                return admin.ProductClassDetailSerializer
            case _:
                raise NotAcceptable()