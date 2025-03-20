from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/user/", include("users.urls")),
    path("api/role/", include("roles.urls")),
    path("api/permission/", include("permissions.urls")),
    path("api/group/", include("posts_groups.urls")),
    path("api/post/", include("posts.urls")),
]
