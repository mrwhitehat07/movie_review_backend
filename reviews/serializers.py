from statistics import mode
from django.forms import fields
from rest_framework import serializers

from user.serializers import ProfileSeriL
from .models import Review
from user.models import Profile, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = '__all__'
    
    # def to_representation(self, instance):
    #     return {
    #         'id': instance.id,
    #         'profile': instance.profile,
    #     }

class UProfileSerial(serializers.ModelSerializer):
    user = UserProfileSerializer()
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # user = UProfileSerial()
    class Meta:
        model = Review
        fields = ['id','rating', 'review', 'timestamp']
        # fields = '__all__'

    # def to_representation(self, value):
    #     return {
    #             'id': value.id,
    #             'fname': value.user,
                # 'lname': value.celebs.lname,
                # 'image': value.celebs.image.url,
                # 'role' : value.role.name,
            # }

class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['rating', 'review']