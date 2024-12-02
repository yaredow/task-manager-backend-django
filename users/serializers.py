from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser


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


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True)

    def save(self, request):
        user = super().save(request)
        user.name = self.validated_data.get("name", "")
        user.save()
        return user
