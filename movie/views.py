from django.http import Http404
from django.http.response import JsonResponse
from pydantic import Json
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from celebs.models import Celebs
from celebs.serializers import CelebritySerializer
from movie.models import Crew, Genre, Movie
from movie.serializers import GenreListSerializer, MovieDetailSerializer, MovieSerializer
from rest_framework.response import Response
from django.db.models import Q

class MovieView(APIView):
    def get(self, request):
        queryset = Movie.objects.all()
        serializer_class = MovieSerializer(queryset, many=True)
        return Response(serializer_class.data)

class MovieDetailView(APIView):
    def get(self, request, pk):
        queryset = Movie.objects.filter(id=pk).first()
        serializer_class = MovieDetailSerializer(queryset, many=False)
        return Response(serializer_class.data)

class GenreView(APIView):
    def get(self, request):
        queryset = Genre.objects.all()
        serializer_class = GenreListSerializer(queryset, many=True)
        return Response(serializer_class.data)

class GenreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    lookup_fields = "pk"

def genre_movie(self, gid):
    movies = Movie.objects.filter(genre=gid)
    serialized_data = MovieSerializer(movies, many=True)
    return JsonResponse(serialized_data.data, safe=False)

def action_movie(self):
    genre = Genre.objects.filter(title="Action").first()
    print(genre)
    movies = Movie.objects.filter(genre=genre.id)
    serialized_data = MovieSerializer(movies, many=True)
    return JsonResponse(serialized_data.data, safe=False)

def get_movie_celebs(self, mid):
    movie = Movie.objects.filter(id=mid).first()
    # crews = []
    # for i in movie.crew.all():
    #     print(i)
    # serializer = MovieCrewSerializer(movie)
    return JsonResponse("serializer.data, safe=False")  
    
def search(self, query):
    movie = Movie.objects.filter(Q(title__icontains=query) | Q(genre__title__icontains=query)).distinct()
    celeb = Celebs.objects.filter(fname__icontains=query).distinct()
    return JsonResponse({ 
        "movie": MovieSerializer(movie, many=True).data,
        "celebs": CelebritySerializer(celeb,many=True).data,
     })