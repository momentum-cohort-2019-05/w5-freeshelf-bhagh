# Generated by Django 2.2.2 on 2019-06-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190625_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, to='core.Category'),
        ),
    ]