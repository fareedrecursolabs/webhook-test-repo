from django.urls import path, include
from .views import PostsView

urlpatterns = [path("", PostsView.as_view(), name="permission")]
