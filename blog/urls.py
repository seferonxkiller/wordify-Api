from django.urls import path
from .views import CategoryApiView, TagApiView, ArticleListCreateAPIView, ArticleTextRUDApiView, ArticleTextCreateApiView, CommentListCreateApiView, ArticleImageCreateApiView, ArticleDetailApiView


urlpatterns =[
    path('', ArticleListCreateAPIView.as_view()),
    path('detail/<int:pk>/', ArticleTextRUDApiView.as_view()),
    path('cat/', CategoryApiView.as_view()),
    path('tag/', TagApiView.as_view()),
    path('article/<int:article_id>/comment-list-create/', CommentListCreateApiView.as_view()),
    path('article_text/<int:article_id>/subtext-list-create/', ArticleTextCreateApiView.as_view()),
    path('article-image/<int:article_text_id>/list-create/', ArticleImageCreateApiView.as_view()),
    path('article-list/<int:pk>/list-rud/', ArticleDetailApiView.as_view()),

]
#
# urlpatterns = [
#     path('blog/<int:pk>/subtext-rud/', SubTextRUDAPIView.as_view()),
#     path('subtext/<int:blog_text_id>/subpicture-list-create/', SubPictureListCreateAPIView.as_view()),
# ]