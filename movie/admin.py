from django.contrib import admin
from movie.models import Movie, Genre, Crew, Notification

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Crew)
admin.site.register(Notification)
