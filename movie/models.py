from django.db import models
from django.db.models.fields import DateField

class Movie(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    poster      = models.ImageField()
    trailer     = models.FileField()
    releasedAt  = DateField()
    
    