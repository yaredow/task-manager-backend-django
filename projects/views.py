from rest_framework import generics
from .models import Project
from .serializer import ProjectSerializer

# Create your views here.


class ListProjectsView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DetailsProjectView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
