from rest_framework import serializers
from .models import *


class TypeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCategory
        fields = ['id', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'type_category', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'get_sub_category', 'name']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'image']


class CategoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_status
        fields = ['id', 'name', 'normalize_title']


class NewValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewValue
        fields = ['id', 'product', 'new_price']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']


class AttributeDetailSerializer(serializers.ModelSerializer):
    new_price = NewValueSerializer(read_only=True)

    class Meta:
        model = AttributeDetail
        fields = ['id',
                  'attribute',
                  'key',
                  'value',
                  'new_price',
                  'made_in',
                  'release_form',
                  'consists',
                  'capacity',
                  'guarantee',
                  ]


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True)
    attribute_detail = AttributeDetailSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id',
                  'status',
                  'name',
                  'category',
                  'brand',
                  'product_images',
                  'attribute_detail',
                  ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }
