from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    # # type_category -->
    # path('1create-type-category/', TypeCategoryCreateAPIView.as_view()),
    # path('1list-type-category/', TypeCategoryListAPIView.as_view()),
    # path('1type-category/<int:pk>/', TypeCategoryRetrieveAPIView.as_view()),
    # path('1type-category/update/<int:pk>/', TypeCategoryUpdateAPIView.as_view()),
    # path('1type-category/destroy/<int:pk>/', TypeCategoryDestroyAPIView.as_view()),

    # # sub_category -->
    # path('2create-sub-category/', SubCategoryCreateAPIView.as_view()),
    # path('2list-sub-category/', SubCategoryListAPIView.as_view()),
    # path('2sub-category/<int:pk>/', SubCategoryRetrieveAPIView.as_view()),
    # path('2sub-category/update/<int:pk>/', SubCategoryUpdateAPIView.as_view()),
    # path('2sub-category/delete/<int:pk>/', SubCategoryDestroyAPIView.as_view()),

    # category -->
    # path('3category/create/', CategoryCreateAPIView.as_view()),
    path('3category/', CategoryListAPIView.as_view()),
    path('3category/<int:pk>/', CategoryRetrieveAPIView.as_view()),
    # path('3category/update<int:pk>/', CategoryUpdateAPIView.as_view()),
    # path('3category/delete/<int:pk>/', CategoryDestroyAPIView.as_view()),

    # brand
    # path('4brand-create/', BrandCreateAPIView.as_view()),
    path('4brand-list/', BrandListAPIView.as_view()),
    path('4brand/<int:pk>/', BrandRetrieveAPIView.as_view()),
    # path('4brand/update/<int:pk>/', BrandUpdateAPIView.as_view()),
    # path('4brand/delete/<int:pk>/', BrandDestroyAPIView.as_view()),

    # product
    path('5product-create/', ProductCreateAPIView.as_view()),
    path('5product/', ProductListAPIView.as_view()),
    path('5product/new/', NewProductListAPIView.as_view()),
    path('5product/<int:pk>/', ProductRetrieveAPIView.as_view()),
    # path('5product/update/<int:pk>/', ProductUpdateAPIView.as_view()),
    # path('5product/delete/<int:pk>/', ProductDestroyAPIView.as_view()),

    # new_value
    # path('6new-price-create/', NewValueCreateAPIView.as_view()),
    path('6new-price-list/', NewValueListAPIView.as_view()),
    path('6new-price/<int:pk>/', NewValueRetrieveAPIView.as_view()),
    # path('6new-price/update/<int:pk>/', NewValueUpdateAPIView.as_view()),
    # path('6new-price/delete/<int:pk>/', NewValueDestroyAPIView.as_view()),
]
