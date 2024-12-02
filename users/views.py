from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework import generics
from .models import CustomUser


# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
