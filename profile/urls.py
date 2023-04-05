from django.urls import path
from rest_framework.authtoken import views

from .views import MyAccount

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('my-account/', MyAccount.as_view()),
]