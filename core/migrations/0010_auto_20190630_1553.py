# Generated by Django 2.2.2 on 2019-06-30 15:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190628_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.AddField(
            model_name='favorite',
            name='favorite_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Book'),
        ),
    ]
