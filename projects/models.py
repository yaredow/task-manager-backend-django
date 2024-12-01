from django.db import models
from cuid import cuid
from users.models import CustomUser

# Create your models here.


class Project(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=cuid,
        editable=False,
    )
    user = models.ForeignKey(
        CustomUser, related_name="projects", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="project_images/",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
