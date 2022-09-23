from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    # category -->
    path('3category/', CategoryListAPIView.as_view()),
    path('3category/<int:pk>/', CategoryRetrieveAPIView.as_view()),

    # brand
    path('4brand-list/', BrandListAPIView.as_view()),
    path('4brand/<int:pk>/', BrandRetrieveAPIView.as_view()),

    # product
    path('5product-create/', ProductCreateAPIView.as_view()),
    path('5product/', ProductListAPIView.as_view()),
    path('5product/new/', NewProductListAPIView.as_view()),
    path('5product/<int:pk>/', ProductRetrieveAPIView.as_view()),

    path('banner/', BannerListAPIView.as_view())
]
