from .views import UserListView, UserDetailView
from django.urls import path

urlpatterns = [
    path("", UserListView.as_view()),
    path("<str:pk>/", UserDetailView.as_view()),
]
