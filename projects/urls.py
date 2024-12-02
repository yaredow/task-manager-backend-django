from django.urls import path
from .views import ProjectsListView, ProjectDetailView

urlpatterns = [
    path("", ProjectsListView.as_view()),
    path("<str:pk>", ProjectDetailView.as_view()),
]
