from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView


urlpatterns = [
    path("", TaskListView.as_view()),
    path(
        "<str:pk>/",
        TaskDetailView.as_view(),
    ),
    path("new/", TaskCreateView.as_view()),
]
