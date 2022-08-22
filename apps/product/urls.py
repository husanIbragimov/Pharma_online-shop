from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    # type_category -->
    path('1create-type-category/', TypeCategoryCreateAPIView.as_view()),
    path('1list-type-category/', TypeCategoryListAPIView.as_view()),
    path('1rud-type-category/<int:pk>/', TypeCategoryRetrieveUpdateDestroyAPIView.as_view()),

    # sub_category -->
    path('2create-sub-category/', SubCategoryCreateAPIView.as_view()),
    path('2list-sub-category/', SubCategoryListAPIView.as_view()),
    path('2rud-sub-category/<int:pk>/', SubCategoryRetrieveUpdateDestroyAPIView.as_view()),

    # category -->
    path('3create-category/', CategoryCreateAPIView.as_view()),
    path('3list-category/', CategoryListAPIView.as_view()),
    path('3rud-category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),

    # brand
    path('4brand-create/', BrandCreateAPIView.as_view()),
    path('4brand-list/', BrandListAPIView.as_view()),
    path('4brand-rud/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view()),

    # product
    path('5product-create/', ProductCreateAPIView.as_view()),
    path('5product-list/', ProductListAPIView.as_view()),
    path('5product-rud/<int:pk>/', ProductRUDAPIView.as_view()),

    # new_value
    path('6new-price-create/', NewValueCreateAPIView.as_view()),
    path('6new-price-list/', NewValueListAPIView.as_view()),
    path('6new-price-rud/<int:pk>/', NewValueRUDAPIView.as_view()),
]
