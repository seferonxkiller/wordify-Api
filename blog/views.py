from django.db.models import Q
from django.shortcuts import render
from .models import Category, Comment, ArticleText, ArticleImage, Tag, Article
from .serializers import TagSerializers, CategorySerializers, MiniArticleSerializers, MiniImagaSerializers, MiniTextSerializers, MiniCommentSerializers, ArticleImageSerializer, ArticleGetSerializers, ArticlePOSTSerializers, CommentSerializer, SubTextSerializer
from rest_framework import generics, permissions


class CategoryApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class TagApiView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()

    def get_queryset(self):
        tc = super().get_queryset()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        tag_condition = Q()
        if tag:
            tag_condition = Q(tags__title__exact=tag)
        cat_condition = Q()
        if category:
            cat_condition = Q(category__title_exact=category)
        tc = tc.filter(tag_condition, cat_condition)
        return tc

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializers
        if self.request.method == 'POST':
            return ArticlePOSTSerializers


class ArticleDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleGetSerializers

    def get_queryset(self):
        tc = super().get_queryset()
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')
        tag_condition = Q()
        if tag:
            tag_condition = Q(tags__title__exact=tag)
        cat_condition = Q()
        if category:
            cat_condition = Q(category__title_exact=category)
        tc = tc.filter(tag_condition, cat_condition)
        return tc


class ArticleTextCreateApiView(generics.ListCreateAPIView):
    queryset = ArticleText.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get("article_id")
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["article_id"] = self.kwargs.get("article_id")
        return ctx

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MiniTextSerializers
        return SubTextSerializer


class ArticleTextRUDApiView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = SubTextSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleImageCreateApiView(generics.ListCreateAPIView):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset()
    #     article_text_id = self.kwargs.get("article_text_id")
    #     if article_text_id:
    #         qs = qs.filter(article_text_id=article_text_id)
    #         return qs
    #     return []
    #
    # def get_serializer_class(self):
    #     ctx = super().get_serializer_class()
    #     ctx["article_text_id"] = self.kwargs.get("article_text_id")
    #     return ctx


class CommentListCreateApiView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx

