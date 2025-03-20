from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Fields displayed in the 'Edit User' page
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "role")}),
        ("Permissions", {"fields": ("permissions", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields shown in the 'Add User' form
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "role", "permissions"),
        }),
    )

    list_display = ("username", "email", "date_of_birth", "role", "is_staff")  # Fields displayed in user list
    search_fields = ("username", "email", "role")  # Enable search by username/email/role
    ordering = ("email",)  # Order users by email
