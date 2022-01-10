from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Celebs(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dob   = models.DateField()
    image = models.ImageField(upload_to='uploads/celebs/')
    role  = models.ManyToManyField(Role)

    def __str__(self) -> str:
        return self.fname + " " + self.lname