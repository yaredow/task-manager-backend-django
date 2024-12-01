from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(max_length=255)

    def save(self, request):
        user = super().save(request)
        user.name = self.data.get("name")
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "full_name", "date_joined", "is_active"]
