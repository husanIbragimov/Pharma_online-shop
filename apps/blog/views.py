from rest_framework import generics, mixins, permissions
from .models import Article
from .serializers import ArticleSerializer
from ..account.permissions import IsAdminUserForAccount


class ArticleMixin(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ArticleCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserForAccount]


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArticleUpdateMixin(ArticleMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'


class ArticleRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserForAccount]
    lookup_field = 'pk'
