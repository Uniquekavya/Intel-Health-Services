
# Create your models here.
from django.db import models

class Hospital(models.Model):
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)
    contactnumber= models.CharField(max_length=50)
    Specialties = models.CharField(max_length=200)
    Websitelink = models.CharField(max_length=100)
       

    def __str__(self):
        return self.Name
    

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    

    

