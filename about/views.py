from rest_framework import generics, views
from rest_framework.response import Response
from blog.models import Article
from blog.serializers import ArticleGetSerializers


class PopularPost(generics.ListAPIView):
    queryset = Article.objects.order_by('-views')[:3]
    serializer_class = ArticleGetSerializers


class MyLatestPost(generics.ListAPIView):
    queryset = Article.objects.order_by('-id')
    serializer_class = ArticleGetSerializers


