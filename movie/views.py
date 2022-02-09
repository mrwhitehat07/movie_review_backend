from django.http import Http404
from django.http.response import JsonResponse
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from movie.models import Genre, Movie
from movie.serializers import GenreListSerializer, MovieCrewSerializer, MovieDetailSerializer, MovieSerializer
from rest_framework.response import Response

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

def get_movie_celebs(self, mid):
    movie = Movie.objects.filter(id=mid).first()
    print(movie)
    serializer = MovieCrewSerializer(movie)
    return JsonResponse(serializer.data, safe=False)  
    
