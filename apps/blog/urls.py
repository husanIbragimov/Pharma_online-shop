from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('article-create', ArticleCreateAPIView.as_view()),
    path('article-list', ArticleListAPIView.as_view()),
    path('article-update/<int:pk>/', ArticleUpdateMixin.as_view()),
    path('article-rd/<int:pk>/', ArticleRetrieveDestroyAPIView.as_view()),
]
