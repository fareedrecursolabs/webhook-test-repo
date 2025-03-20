from django.shortcuts import render
from rest_framework import generics
from .serializer import RoleSerializer
from .models import Role
from common.permissions import IsAdminRole
from common.authentication import QueryParamJWTAuthentication

class RoleView(generics.ListCreateAPIView):
  serializer_class = RoleSerializer
  queryset = Role.objects.all()
  permission_classes = [IsAdminRole]
  authentication_classes = [QueryParamJWTAuthentication]

  def custom_permission(self, permission_name):
    user_permissions = self.request.user.permissions.all()
    if permission_name in user_permissions:
      return True
    return False
