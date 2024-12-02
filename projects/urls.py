from django.urls import path
from .views import ProjectsListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path("", ProjectsListView.as_view()),
    path("new/", ProjectCreateView.as_view()),
    path("<str:pk>/", ProjectDetailView.as_view()),
]
