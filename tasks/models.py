from django.db import models
from cuid import cuid
from projects.models import Project

# Create your models here.


class TaskStatus(models.TextChoices):
    BACKLOG = "BACKLOG", "Backlog"
    TODO = "TODO", "To Do"
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    IN_REVIEW = "IN_REVIEW", "In Review"
    DONE = "DONE", "Done"


class Task(models.Model):
    id = models.CharField(
        max_length=75,
        primary_key=True,
        default=cuid,
        editable=False,
    )
    status = models.CharField(
        max_length=30,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def owner(self):
        return self.project.user
