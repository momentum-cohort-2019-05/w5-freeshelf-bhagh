from django.contrib import admin

# Register your models here.
from core.models import Book, Author, Category, Favorite

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Favorite)