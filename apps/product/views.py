from rest_framework import generics, status, response, viewsets, mixins, permissions, authentication
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


class TypeCategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TypeCategory.objects.all()
    serializer_class = TypeCategorySerializer
    lookup_field = 'pk'


class TypeCategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = TypeCategory.objects.all()
    serializer_class = TypeCategorySerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class TypeCategoryDestroyAPIView(generics.DestroyAPIView):
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


class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class SubCategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class SubCategoryDestroyAPIView(generics.DestroyAPIView):
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


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'pk'


class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class CategoryDestroyAPIView(generics.DestroyAPIView):
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


class BrandRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class BrandUpdateAPIView(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class BrandDestroyAPIView(generics.DestroyAPIView):
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
    authentication_classes = (authentication.TokenAuthentication,)
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset_list = super().get_queryset().filter()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title_icontains=query) |
                Q(status=query) |
                Q(category__name=query)
            )
        return queryset_list


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductDestroyAPIView(generics.DestroyAPIView):
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


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class NewValueCreateAPIView(generics.CreateAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    permission_classes = [IsAdminUserForAccount]


class NewValueListAPIView(generics.ListAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer


class NewValueRetrieveAPIView(generics.RetrieveAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    lookup_field = 'pk'


class NewValueUpdateAPIView(generics.UpdateAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class NewValueDestroyAPIView(generics.DestroyAPIView):
    queryset = NewValue.objects.all()
    serializer_class = NewValueSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'
