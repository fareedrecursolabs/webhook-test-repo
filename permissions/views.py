from django.shortcuts import render
from rest_framework import generics
from .models import Permission
from .serializer import PermissionSerialization
from rest_framework.permissions import IsAuthenticated


class PermissionView(generics.ListCreateAPIView):
  serializer_class = PermissionSerialization
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    if serializer.is_valid():
       serializer.save(created_by=self.request.user)

  def get_queryset(self):
    return Permission.objects.filter(created_by=self.request.user)
