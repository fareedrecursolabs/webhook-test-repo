from rest_framework import generics, viewsets
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Post
# Create your views here.


class PostsView(generics.ListCreateAPIView):
  serializer_class = PostSerializer
  # permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    posts_group_id = self.request.data['posts_group']
    if serializer.is_valid():
       serializer.save(posts_group=posts_group_id, author=self.request.user)

  def get_queryset(self):
    posts_group_id = self.request.data['posts_group']
    return Post.objects.filter(posts_group=posts_group_id)


class PostsViewSet(viewsets.ReadOnlyModelViewSet):
  serializer_class = PostSerializer
