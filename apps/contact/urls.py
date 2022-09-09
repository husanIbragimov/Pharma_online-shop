from django.urls import path
from .views import GetInTouchCreateAPIView, SubscribeCreateAPIView

app_name = 'contact'

urlpatterns = [
    path('create/', GetInTouchCreateAPIView.as_view()),
    path('subscribe/', SubscribeCreateAPIView.as_view())
]
