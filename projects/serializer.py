from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "image", "created_at", "updated_at"]

    def create(self, validated_data):
        print("logged user", self.context["request"].user)
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
