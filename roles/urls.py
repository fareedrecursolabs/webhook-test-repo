from django.urls import path, include
from .views import RoleView

urlpatterns = [path("", RoleView.as_view(), name="role")]
