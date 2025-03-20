from django.db import models
from users.models import CustomUser
from posts_groups.models import PostsGroup
import uuid


class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(blank=False, null=False, max_length=100)
  description = models.TextField(blank=True, null=True)
  author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="post_created_by", blank=False, null=False, to_field='id')
  posts_group = models.ForeignKey(PostsGroup, on_delete=models.CASCADE, related_name="post_created_by", blank=False, null=False, to_field='id')

  def __str__(self):
    return self.title
