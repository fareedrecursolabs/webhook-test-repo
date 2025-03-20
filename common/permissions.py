from rest_framework import permissions

class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        print("Authenticated User:", request.user)
        user_permissions = request.user.permissions.all()  # Use `.all()` for ManyToManyField

        print(user_permissions)
        return request.user.is_authenticated and request.user.role.name.lower() == "admin"


