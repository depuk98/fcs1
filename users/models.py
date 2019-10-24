from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser): 
    age = models.PositiveIntegerField(default=0)



class Post(models.Model): 
    title = models.CharField(max_length=200) 
    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, ) 
    body = models.TextField()
    def __str__(self): 
        return self.title
