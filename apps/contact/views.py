from .models import GetInTouch, Subscribe
from rest_framework import generics, permissions
from .serializers import GetInTouchSerializer, SubscribeSerializer


class GetInTouchCreateAPIView(generics.CreateAPIView):
    queryset = GetInTouch.objects.all()
    serializer_class = GetInTouchSerializer


class SubscribeCreateAPIView(generics.CreateAPIView):
    queryset = Subscribe.objects.filter(is_active=True).order_by('-id')
    serializer_class = SubscribeSerializer

