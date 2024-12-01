from django.shortcuts import render
from rest_framework import generics
from .models import Project

# Create your views here.


class ListProjectsView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
