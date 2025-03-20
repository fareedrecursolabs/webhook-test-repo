from rest_framework import generics
from .serializer import PostsGroupSerializer
from .models import PostsGroup

class PostsGroupView(generics.ListCreateAPIView):
  serializer_class = PostsGroupSerializer
  queryset = PostsGroup.objects.all()

class PostsGroupIdView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = PostsGroupSerializer
  queryset = PostsGroup.objects.all()
