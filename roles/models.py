from django.db import models
import uuid


class Role(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(unique=True, null=False, blank=False, max_length=30)

  def __str__(self):
    return self.name
