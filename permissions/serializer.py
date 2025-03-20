from rest_framework import serializers
from .models import Permission

class PermissionSerialization(serializers.ModelSerializer):

  class Meta:
    model = Permission
    fields = ['id', 'name']

  def create(self, validated_data):
    validated_data['name'] = validated_data['name'].lower().replace(" ", "_")
    return super().create(validated_data)

  def update(self, instance, validated_data):
        """Modify name and update the instance"""
        instance.name = validated_data.get('name', instance.name).lower().replace(" ", "_")
        instance.save()
        return instance
