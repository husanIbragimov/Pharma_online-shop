from rest_framework.generics import get_object_or_404

from .serializers import WishListSerializer, WishListCreateSerializer, CartItemSerializer, \
    OrderSerializer
from rest_framework import generics, status, permissions, views
from rest_framework.response import Response
from django.http import JsonResponse
from .models import *
from apps.product.models import Product


class WishListListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/carts/api/wishlist/list-create/
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return super().get_queryset().filter(user_id=user_id)

    def create(self, request, *args, **kwargs):
        serializer = WishListCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user_id = self.request.user.id
        serializer.save(user_id=user_id)


class AddToCartItemCreateAPIView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItemSerializer


# class MyCartListAPIView(generics.ListAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#     def get_queryset(self):
#         qs = super().get_queryset().filter(client=self.request.user, is_ordered=False)
#         return qs


class DeleteFromMyCart(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class RetrieveMyCart(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        data['client'] = request.user.id
        print(request.user.id)
        print(data)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     cart_id = request.data.get('cart_id')
    #     cart = Cart.objects.filter(id=cart_id).first()
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(client_id=request.user.id, cart_id=cart.id)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class QuantityUpdateAPIView(generics.RetrieveAPIView):
    queryset = CartItem.objects.all()

    def patch(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.quantity = request.data['quantity']
        instance.save()
        return Response({'success': True, 'quantity': instance.quantity})
