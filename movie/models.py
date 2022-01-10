# django core import
from django.db import models
from celebs.models import Role, Celebs

class Crew(models.Model):
    role   = models.ForeignKey(Role, on_delete=models.CASCADE)
    celebs = models.ForeignKey(Celebs, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.role.name + "->" + self.celebs.fname

class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

class Movie(models.Model):
    title           = models.CharField(unique=True, max_length=255)
    description     = models.TextField()
    poster          = models.ImageField(upload_to='uploads/posters/')
    trailer         = models.FileField(upload_to='uploads/trailers/')
    running_time    = models.CharField(max_length=255, null=True)
    genre           = models.ManyToManyField(Genre)
    crew            = models.ManyToManyField(Crew)
    release_date    = models.DateField()
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title