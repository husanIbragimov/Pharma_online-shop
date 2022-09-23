from django.urls import path
from . import views


urlpatterns = [
    path('item-add/', views.AddToCartItemCreateAPIView.as_view()),
    path('my-cart/<int:pk>/', views.DeleteFromMyCart.as_view()),
    path('order/', views.OrderAPIView.as_view()),
    path('quantity/', views.QuantityUpdateAPIView.as_view()),
]