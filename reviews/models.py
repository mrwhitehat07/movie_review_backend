from django.db import models
from django.conf import settings
from movie.models import Movie

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.TextField()
    review = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

