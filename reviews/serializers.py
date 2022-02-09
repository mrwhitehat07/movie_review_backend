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
        # fields = ['user', 'rating', 'review']
        fields = '__all__'

class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'review']