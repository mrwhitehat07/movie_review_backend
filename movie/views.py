from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from movie.models import Genre, Movie
from movie.serializers import GenreListSerializer, MovieDetailSerializer, MovieSerializer


class MovieView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_fields = "pk"

class GenreView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer

class GenreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    lookup_fields = "pk"

def genre_movie(self, gid):
    movies = Movie.objects.filter(genre=gid)
    serialized_data = MovieSerializer(movies, many=True)
    return JsonResponse(serialized_data.data, safe=False)
