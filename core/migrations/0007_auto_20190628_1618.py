# Generated by Django 2.2.2 on 2019-06-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='times_favorited',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
