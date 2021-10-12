from django.db import models

class user(models.Model):
    name = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    
# Create your models here.
