from django.contrib.auth.models import Group, User
from django.db.models import fields, manager
from rest_framework import serializers
from .models import Profile, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def getModel(self):
        return self.Meta.model.object.email

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data)
        user_obj = UserProfile.objects.create_user(**user_data)
        user_obj.set_password(user_obj.password)
        user_obj.save()
        my_group = Group.objects.get(name='user')
        my_group.user_set.add(user_obj)
        profile = Profile.objects.create(user=user_obj, **validated_data)
        return profile
        # return user_obj


class ProfileSeriL(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields= ['fname', 'lname', 'phone', 'avatar',]

class UserSer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['id','username','email']

