from statistics import mode
from django.forms import fields
from rest_framework import serializers
from .models import Review
from user.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class ReviewSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer()
    class Meta:
        model = Review
        fields = ['rating', 'review', 'timestamp']
        # fields = '__all__'

    # def to_representation(self, value):
    #     return {
    #             'id': value.id,
    #             'fname': value.user.profile,
    #             # 'lname': value.celebs.lname,
    #             # 'image': value.celebs.image.url,
    #             # 'role' : value.role.name,
    #         }

class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'review']