from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)
    #slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, default="", null=True)
    category = models.ManyToManyField(Category)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500, help_text='Enter a brief description of the book')  
    url = models.URLField(max_length=300, blank=True)
    times_favorited = models.PositiveIntegerField(default=0)
    favorited_by = models.ManyToManyField(to=User, related_name='favorite_books', through='Favorite')

    #image_url = models.URLField(max_length=300)

    class Meta:
        ordering = ["-date"]
 
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Author(models.Model):
    name = models.CharField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Favorite (models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book,on_delete=models.CASCADE)
    favorite_at = models.DateTimeField(default=datetime.now, blank=True)



