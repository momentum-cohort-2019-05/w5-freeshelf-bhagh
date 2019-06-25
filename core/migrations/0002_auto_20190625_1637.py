from django.db import migrations
from django.conf import settings
import os
import csv


def load_books(apps, schema_editor):
    Book = apps.get_model('core', 'Book')
    Author = apps.get_model('core', 'Author')
    book = Book()
    book.save()
    filename = os.path.join(settings.BASE_DIR, 'sample_books.csv')
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            author = Author(name=row['author'])
            author.save()
            book = Book(title=row['title'], author=author, url=row['url'], description=row['description'])
            book.save()
    

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [migrations.RunPython(load_books)]