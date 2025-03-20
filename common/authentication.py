from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from users.models import CustomUser


class QueryParamJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Check for token in Authorization header first
        header_auth = super().authenticate(request)
        print('header_auth',header_auth)
        if header_auth:
            return header_auth  # If found in header, use it

        # Otherwise, check for token in query parameters (for testing only)
        token = request.GET.get("token")
        print(f"🔍 Received token: {token}")  # Debug

        if token:
            try:
                decoded_token = AccessToken(token)  # Decode JWT
                user_id = decoded_token["user_id"]
                # user = self.get_user(decoded_token)  # Retrieve user from token
                user = CustomUser.objects.get(id=user_id)
                return (user, decoded_token)  # Authenticate user
            except Exception as e:
                raise AuthenticationFailed("Invalid token")

        return None  # No token found
