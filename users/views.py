from rest_framework import generics
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
