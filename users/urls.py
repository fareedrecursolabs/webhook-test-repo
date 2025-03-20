from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateUserView, UsersListView


urlpatterns = [
  path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("register/", CreateUserView.as_view(), name="register_user"),
    path("", UsersListView.as_view(), name="user_list"),
]
