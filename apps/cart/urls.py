from django.urls import path
from . import views


urlpatterns = [
    path('wishlist/list-create/', views.WishListListCreateAPIView.as_view()),
    path('item-add/', views.AddToCartItemCreateAPIView.as_view()),
    # path('cart/', views.CartItemListAPIView.as_view()),
    path('my-cart/<int:pk>/', views.DeleteFromMyCart.as_view()),
    path('order/', views.OrderAPIView.as_view()),
    path('quantity/<int:pk>/', views.QuantityUpdateAPIView.as_view()),
]
