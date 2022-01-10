from django.db import models
from rest_framework import serializers
from movie.models import Crew, Movie, Genre
from celebs.models import Celebs

class CelebsSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return (value.celebs.fname + value.celebs.lname)

    class Meta:
        model = Celebs
        fields = ['fname', 'lname']

class CrewSerializer(serializers.RelatedField):
    celebs = CelebsSerializer()
    class Meta:
        model = Crew
        fields = ['id', 'role', 'celebs']

    def to_representation(self, value):
        return {
                'id': value.id,
                'fname': value.celebs.fname,
                'lname': value.celebs.lname,
                'image': value.celebs.image.url,
                'role' : value.role.name,
            }

class GenreSerializer(serializers.RelatedField):
    class Meta:
        model = Genre
        fields = ['title']

    def to_representation(self, value):
        return value.title

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster', 'release_date']


class MovieDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    crew  = CrewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'trailer', 'release_date', 'genre', 'crew']

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
