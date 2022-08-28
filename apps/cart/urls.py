from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('wishlist/', WishListListCreateAPIView.as_view()),
    path('order-save/', OrderAPIView.as_view()),
    path('order-get/', OrderListAPI.as_view()),
    path('order-delete/', OrderDestroyAPI.as_view()),
]
