from django.contrib import admin
from .models import Category, Tag, Article, ArticleText, ArticleImage, Comment

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)