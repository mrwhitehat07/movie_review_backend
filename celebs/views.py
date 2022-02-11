import json
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from celebs.models import Celebs, Role
from celebs.serializers import CelebritySerializer, RoleSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from movie.models import Movie
from movie.serializers import MovieSerializer
from rest_framework.views import APIView

class CelebrityListView(APIView):
    def get(self, request):
        queryset = Celebs.objects.all()
        serializer_class = CelebritySerializer(queryset, many=True)
        return Response(serializer_class.data)

class CelebrityDetailView(APIView):
    def get(self, request, pk):
        queryset = Celebs.objects.filter(id=pk).first()
        movies = Movie.objects.filter(crew=pk)
        serializer_class = CelebritySerializer(queryset, many=False)
        # return Response({
        #     "celebs": serializer_class.data,
        #     "movies": movie_class.data
        # })
        return Response(serializer_class.data)

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
