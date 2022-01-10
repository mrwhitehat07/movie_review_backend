import json
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from celebs.models import Celebs, Role
from celebs.serializers import CelebritySerializer, RoleSerializer
from django.http import JsonResponse

from movie.models import Movie
from movie.serializers import MovieSerializer

class CelebrityListView(ListAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebritySerializer

class CelebrityDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Celebs.objects.all()
    serializer_class = CelebritySerializer
    lookup_fields = "pk"

class RoleView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_fields = "pk"

def celebs_movies(self, cid):
    movies = Movie.objects.filter(crew=cid)
    serialized_movies = MovieSerializer(movies, many=True)
    return JsonResponse(serialized_movies.data, safe=False)
