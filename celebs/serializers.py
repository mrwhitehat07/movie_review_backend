from django.db.models import fields
from rest_framework import serializers
from celebs.models import Celebs, Role

class CelebsRoleSerializer(serializers.RelatedField):
    class Meta:
        model = Role
        fields = ["name"]

    def to_representation(self, value):
        return value.name

class CelebritySerializer(serializers.ModelSerializer):
    role = CelebsRoleSerializer(many=True, read_only=True)
    class Meta:
        model = Celebs
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'