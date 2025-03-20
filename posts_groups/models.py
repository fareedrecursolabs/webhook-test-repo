from django.db import models
from users.models import CustomUser
from permissions.models import Permission
import uuid

class PostsGroup(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50, null=False, blank=False)
  admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="admin_groups", to_field='id')
  permissions = models.ManyToManyField(Permission, related_name="groups_permissions", blank=True)

  def __str__(self):
    return self.name
