from rest_framework import generics, status, response, viewsets, mixins, permissions, authentication
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .models import *
from .serializers import *
from ..account.permissions import IsAdminUserForAccount


# class TypeCategoryCreateAPIView(generics.CreateAPIView):
#     queryset = TypeCategory.objects.all()
#     serializer_class = TypeCategorySerializer
#     permission_classes = [IsAdminUserForAccount]
#
#
# class TypeCategoryListAPIView(generics.ListAPIView):
#     queryset = TypeCategory.objects.all()
#     serializer_class = TypeCategorySerializer
#
#
# class TypeCategoryRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = TypeCategory.objects.all()
#     serializer_class = TypeCategorySerializer
#     lookup_field = 'pk'
#
#
# class TypeCategoryUpdateAPIView(generics.UpdateAPIView):
#     queryset = TypeCategory.objects.all()
#     serializer_class = TypeCategorySerializer
#     permission_classes = [IsAdminUserForAccount]
#     lookup_field = 'pk'
#
#
# class TypeCategoryDestroyAPIView(generics.DestroyAPIView):
#     queryset = TypeCategory.objects.all()
#     serializer_class = TypeCategorySerializer
#     permission_classes = [IsAdminUserForAccount]
#     lookup_field = 'pk'
#
#
# class SubCategoryCreateAPIView(generics.CreateAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#     permission_classes = [IsAdminUserForAccount]
#
#
# class SubCategoryListAPIView(generics.ListAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#     permission_classes = [IsAdminUserForAccount]
#     lookup_field = 'pk'
#
#
# class SubCategoryUpdateAPIView(generics.UpdateAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#     permission_classes = [IsAdminUserForAccount]
#     lookup_field = 'pk'
#
#
# class SubCategoryDestroyAPIView(generics.DestroyAPIView):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategorySerializer
#     permission_classes = [IsAdminUserForAccount]
#     lookup_field = 'pk'


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True, parent_category__isnull=True).order_by('name')
    serializer_class = CategorySerializer
    authentication_classes = (authentication.TokenAuthentication,)


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    lookup_field = 'pk'


class BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserForAccount]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True).order_by('-id')
    serializer_class = ProductSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        qs = self.queryset.all()
        param = self.request.GET.get('search')
        cat = self.request.GET.get('category')

        param_condition = Q()
        if param:
            param_condition = Q(name__icontains=param)
        cat_condition = Q()
        if cat:
            cat_condition = Q(category__name__icontains=cat)

        qs = qs.filter(param_condition, cat_condition)
        return qs


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class NewProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    serializer_class = ProductSerializer


class NewValueListAPIView(generics.ListAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer


class NewValueRetrieveAPIView(generics.RetrieveAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    lookup_field = 'pk'

