from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny
from .models import CustomUser

# Create your views here.


class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  queryset = CustomUser.objects.all()
  permission_classes = [AllowAny]


class UsersListView(generics.ListAPIView):
  serializer_class = UserSerializer
  queryset = CustomUser.objects.all()
  permission_classes = [AllowAny]
