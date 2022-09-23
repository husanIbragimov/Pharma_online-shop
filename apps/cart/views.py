from .serializers import CartItemSerializer, OrderSerializer
from rest_framework import generics, status, permissions, views
from rest_framework.response import Response
from .models import Order, CartItem


class AddToCartItemCreateAPIView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


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
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class QuantityUpdateAPIView(views.APIView):

    def post(self, request, *args, **kwargs):
        for i, j in zip(request.data['cart_items'], request.data['quantities']):
            try:
                obj = CartItem.objects.get(id=i)
            except (CartItem.DoesNotExist, CartItem.MultipleObjectsReturned):
                return Response({'error': 'Cart Item does not exist'})
            obj.quantity = j
            obj.save()
        return Response({'message': 'Cart items quantities successfully updated'}, status=status.HTTP_200_OK)
