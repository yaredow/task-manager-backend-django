from django.test import TestCase
from users.models import CustomUser
from .models import Project

# Create your tests here.


class TestProjectModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            name="John Doe",
            email="johndoe@gmail.com",
            password="test123",
        )

        self.project = Project.objects.create(
            name="test project",
            user=self.user,
        )

    def test_project_belong_to_user(self):
        self.assertEqual(self.project.user, self.user)
        self.assertEqual(self.project.name, "test project")

    def test_create_project(self):
        project = Project.objects.create(user=self.user, name="test project 2")
        self.assertEqual(Project.objects.count(), 2)
        self.assertEqual(project.name, "test project 2")
        self.assertEqual(project.user, self.user)

    def test_read_project(self):
        project = Project.objects.get(name="test project")
        self.assertEqual(project, self.project)
        self.assertEqual(self.user, project.user)

    def test_update_project(self):
        self.project.name = "test updated project"
        self.project.save()
        updated_project = Project.objects.get(id=self.project.id)
        self.assertEqual(updated_project.name, "test updated project")

    def test_delete_project(self):
        self.project.delete()
        self.assertEqual(Project.objects.count(), 0)
