from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()

# Create your views here.

class Register(generics.CreateAPIView):
    serializer_class = UserSerializer
