from .models import GetInTouch, Subscribe
from rest_framework import generics, permissions
from .serializers import GetInTouchSerializer, SubscribeSerializer


class GetInTouchCreateAPIView(generics.CreateAPIView):
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#
# class SubscribeCreateAPIView(generics.CreateAPIView):
#     queryset = Subscribe.objects.all()
#     serializer_class = SubscribeSerializer

