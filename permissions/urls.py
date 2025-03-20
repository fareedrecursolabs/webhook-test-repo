from django.urls import path, include
from .views import PermissionView

urlpatterns = [path("", PermissionView.as_view(), name="permission")]
