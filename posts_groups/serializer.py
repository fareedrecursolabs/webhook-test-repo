from rest_framework import serializers
from .models import PostsGroup

class PostsGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostsGroup
    fields = ['id', 'name', 'admin', 'permissions']
