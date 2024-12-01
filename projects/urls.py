from django.urls import path
from .views import ListProjectsView, DetailsProjectView

urlpatterns = [
    path("", ListProjectsView.as_view()),
    path("<str:pk>", DetailsProjectView.as_view()),
]
