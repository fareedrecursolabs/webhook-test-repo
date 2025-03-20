from django.contrib import admin
from .models import Permission
from django.contrib.auth.models import Group


class PermissionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Permission, PermissionAdmin)
admin.site.unregister(Group)
