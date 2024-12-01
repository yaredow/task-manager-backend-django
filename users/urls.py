from django.urls import path
from .views import DetailUserView

urlpatterns = [path("me/", DetailUserView.as_view())]
