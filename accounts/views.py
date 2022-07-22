from rest_framework import generics
from .models import CustomUser

from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

