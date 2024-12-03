"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/projects/", include("projects.urls")),
    path("api/v1/tasks/", include("tasks.urls")),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path(
        "api/v1/auth/registration/",
        include("dj_rest_auth.registration.urls"),
    ),
    path("api/v1/auth/jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("api/v1/auth/jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("api/v1/auth/jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
