from django.urls import path
from movie.views import GenreDetailView, GenreView, MovieDetailView, MovieView, genre_movie

urlpatterns = [
    path('movie/', MovieView.as_view(), name="movie"),
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movie-detail"),
    path('genre/', GenreView.as_view(), name="genre"),
    path('genre/<int:pk>', GenreDetailView.as_view(), name="genre-detail"),
    path('genre/<int:gid>/movies', genre_movie, name="genre-movie"),
]