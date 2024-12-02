from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import CustomUser
from projects.models import Project


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = ("id", "email", "name", "is_active")


class UserSerializer(serializers.ModelSerializer):
    """projects = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Project.objects.all()
    )"""

    class Meta:
        model = CustomUser
        fields = ("id", "email", "name", "is_active")
