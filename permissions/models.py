from django.db import models
from users.models import CustomUser
import uuid

# Create your models here.

class Permission(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(unique=True, null=False, blank=False, max_length=50)
  created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="created_by_user", to_field='id')
  # parent_permission = models.ForeignKey("self", on_delete=models.CASCADE,null=False,  # Root categories will have null parent
  #       blank=False, default=1, related_name="parent")


  def __str__(self):
    return self.name
