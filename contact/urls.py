from django.urls import path
from .views import ContactListView

urlpatterns = [
    path('list/', ContactListView.as_view()),
]