# Generated by Django 2.2.2 on 2019-06-30 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190630_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['favorite_at']},
        ),
    ]
