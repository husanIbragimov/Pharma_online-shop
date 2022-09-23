from rest_framework import serializers
from .models import CartItem, Order
from apps.product.serializers import ProductSerializer


class CartItemReadSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'get_total']


class OrderSerializer(serializers.ModelSerializer):
    summa = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    quantity = serializers.SerializerMethodField(read_only=True)

    def get_quantity(self, obj):
        return obj.get_quantity

    def get_summa(self, obj):
        return obj.get_summa

    class Meta:
        model = Order
        fields = ['id', 'client', 'cart_items', 'quantity', 'summa', 'phone', 'address', 'zipcode', 'note', 'created_at']

