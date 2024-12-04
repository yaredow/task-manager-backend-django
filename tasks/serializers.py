from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "status",
            "description",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
            "project",
        ]
