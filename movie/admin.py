from django.contrib import admin
from movie.models import Movie, Genre, Crew

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Crew)
