from rest_framework import generics, status, response, viewsets, mixins, permissions
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .models import *
from .serializers import *
from ..account.permissions import IsAdminUserForAccount


class TypeCategoryCreateAPIView(generics.CreateAPIView):
    queryset = TypeCategory.objects.all()
    serializer_class = TypeCategorySerializer
    permission_classes = [IsAdminUserForAccount]


class TypeCategoryListAPIView(generics.ListAPIView):
    queryset = TypeCategory.objects.all()
    serializer_class = TypeCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TypeCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeCategory.objects.all()
    serializer_class = TypeCategorySerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class SubCategoryCreateAPIView(generics.CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUserForAccount]


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SubCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUserForAccount]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class BrandCreateAPIView(generics.CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUserForAccount]


class BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserForAccount]


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset_list = super().get_queryset().filter()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title_icontains=query) |
                Q(status=query) |
                Q(category=query)
            )
        return queryset_list


class ProductRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class NewValueCreateAPIView(generics.CreateAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    permission_classes = [IsAdminUserForAccount]


class NewValueListAPIView(generics.ListAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    permission_classes = [permissions.IsAuthenticated]


class NewValueRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'




