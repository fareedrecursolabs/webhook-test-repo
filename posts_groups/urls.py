from django.urls import path
from .views import PostsGroupView, PostsGroupIdView

urlpatterns = [
  path("", PostsGroupView.as_view(), name="posts_groups"),
  path("<uuid:pk>/", PostsGroupIdView.as_view(), name="posts_groups_by_id")
]
