from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from roles.models import Role
import uuid

class CustomUser(AbstractUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  date_of_birth = models.DateField(null=True, blank=True)

  email = models.EmailField(_("email address"), unique=True)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users", to_field='id')
  permissions = models.ManyToManyField(
        'permissions.Permission',
        related_name="users_permissions",
        blank=True
    )
  posts_groups = models.ManyToManyField(
        'posts_groups.PostsGroup',
        related_name="members",
        blank=True
    )

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = CustomUserManager()

  def __str__(self):
    return self.email
