from rest_framework import serializers
from .models import *
from apps.account.serializers import AccountSerializer
from apps.product.serializers import ProductSerializer


class WishListSerializer(serializers.ModelSerializer):
    user = AccountSerializer(required=False)
    product = ProductSerializer(required=False)

    class Meta:
        model = WishList
        fields = ['id', 'user', 'product']


class WishListCreateSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email', read_only=True)

    # product_sz = serializers.SerializerMethodField(read_only=True)

    # def get_product_sz(self, obj):
    #     product = obj.product
    #     product_sz = ProductSerializer(product)
    #     return product_sz.data

    class Meta:
        model = WishList
        fields = ['id', 'user', 'user_email', 'product']  # <-- 'product_sz'
        extra_kwargs = {
            "user": {"required": False}
        }


class CartItemReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total']


# class CartSerializer(serializers.ModelSerializer):
#     client_email = serializers.CharField(source='client.email', read_only=True)
#     cart_items = serializers.SerializerMethodField()
#
#     def get_cart_items(self, obj):
#         qs = CartItem.objects.filter(cart_id=obj.id)
#         sz = CartItemReadSerializer(qs, many=True)
#         return sz.data
#
#     class Meta:
#         model = Cart
#         fields = ['id', 'client_email', 'is_ordered', 'get_cart_items', 'cart_items', 'get_cart_total']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total']


class OrderSerializer(serializers.ModelSerializer):
    summa = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    # client = serializers.CharField(source='client.email', read_only=True)
    quantity = serializers.SerializerMethodField(read_only=True)

    def get_quantity(self, obj):
        return obj.get_quantity

    def get_summa(self, obj):
        return obj.get_summa

    class Meta:
        model = Order
        fields = ['id', 'client', 'cart_items', 'quantity', 'summa', 'phone', 'address', 'zipcode', 'note', 'created_at']

