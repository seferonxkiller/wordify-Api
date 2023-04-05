from django.urls import path
from .views import PopularPost, MyLatestPost

urlpatterns = [
    path('popular-posts/', PopularPost.as_view()),
    path('latest    -posts/', MyLatestPost.as_view())
]