from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(write_only=True)
  date_of_birth = serializers.DateField(required=True)

  class Meta:
    model = CustomUser
    fields = ['username','email', 'password', 'confirm_password', 'date_of_birth', 'role', 'permissions']
    extra_kwargs = {"password": {"write_only": True}}

  def validate(self, data):

    if data["password"] != data["confirm_password"]:
        raise serializers.ValidationError({"confirm_password": "Passwords do not match."})

    try:
        validate_password(data["password"])
    except ValidationError as e:
        raise serializers.ValidationError({"password": e.messages})

    return data

  def create(self, validated_data):
    validated_data.pop("confirm_password")
    user = CustomUser.objects.create_user(**validated_data)
    return user
