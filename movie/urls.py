from django.urls import path
from movie.views import GenreDetailView, GenreView, MovieDetailView, MovieView, NotificationView, action_movie, genre_movie, get_movie_celebs, search
from reviews.views import UpdateReview, movie_reviews, Reviews, reviews

urlpatterns = [
    path('movie/', MovieView.as_view(), name="movie"),
    path('movie/action', action_movie, name="movie"),
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movie-detail"),
    path('genre/', GenreView.as_view(), name="genre"),
    path('genre/<int:pk>', GenreDetailView.as_view(), name="genre-detail"),
    path('genre/<int:gid>/movies', genre_movie, name="genre-movie"),
    path('movie/<int:pk>/reviews', movie_reviews, name="movie-reviews"),
    # path('movie/<int:mid>/crew', get_movie_celebs, name="movie-crew"),
    path('reviews/<int:rid>', reviews, name="reviews"),
    path('movie/<int:pk>/reviews/post', Reviews.as_view(), name="post-movie-reviews"),
    path('movie/<int:pk>/reviews/update/<int:rid>', UpdateReview.as_view(), name="update-movie-reviews"),
    path('search/q=<str:query>', search, name='search'),
    path('notifications/', NotificationView.as_view(), name='notifications')
]