from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from apps.product.models import Category, Option, ProductClass


class CreateCategorySerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False)
    slug = serializers.SlugField(required=False)

    def create(self, validated_data):
        parent = validated_data.pop('parent', None)

        if parent is None:
            instance = Category.add_root(**validated_data)
        else:
            parent_node = get_object_or_404(Category, pk=parent)
            instance = parent_node.add_child(**validated_data)
        return instance

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'is_active', 'slug', 'parent')


class CategoryListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'is_active', 'slug', 'children')

    def get_children(self, obj):
        return CategoryListSerializer(obj.get_children(), many=True).data


class CategoryDetailSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_children(self, obj):
        return CategoryListSerializer(obj.get_children(), many=True).data


class CategoryUpdateOrDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'is_active')


class OptionProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'title', 'type', 'is_required')

class ProductClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductClass
        fields = ('id', 'title', 'description', 'is_active', 'track_stock', 'is_shipping')

class ProductClassDetailSerializer(serializers.ModelSerializer):
    option = OptionProductListSerializer(many=True)

    class Meta:
        model = ProductClass
        fields = '__all__'