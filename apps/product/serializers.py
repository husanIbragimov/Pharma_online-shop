from rest_framework import serializers
from .models import *


# class TypeCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TypeCategory
#         fields = ['id', 'name']
#
#
# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = ['id', 'type_category', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'parent_category', 'name']


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        qs = Category.objects.filter(parent_category=obj, is_active=True)
        sz = SubCategorySerializer(qs, many=True)
        return sz.data

    class Meta:
        model = Category
        fields = ['id', 'name', 'children']


#
#
# class CategorySerializer(serializers.ModelSerializer):
#     font_type = serializers.SlugRelatedField(many=True, slug_field='children', read_only=True)
#
#     class Meta:
#         model = Category
#         fields = ['id', 'parent_category', 'name', 'font_type']


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
        fields = ['id', 'new_price']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id',
                  'get_image_url'
                  ]


class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True)
    category = CategorySerializer(many=True, read_only=True)

    # def get_images(self, obj):
    #     qs = ProductImage.objects.filter(is_active=True, product=obj)
    #     sz = ProductImageSerializer(instance=qs, many=True)
    #     return sz.data

    class Meta:
        model = Product
        fields = ['id',
                  'status',
                  'name',
                  'category',
                  'brand',
                  'key',
                  'value',
                  'sale',
                  'made_in',
                  'release_form',
                  'consists',
                  'capacity',
                  'guarantee',
                  'product_images',
                  ]
        extra_kwargs = {
            'slug': {'read_only': True}
        }


class BannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = ['image']
