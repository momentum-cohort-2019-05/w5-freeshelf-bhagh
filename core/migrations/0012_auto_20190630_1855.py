# Generated by Django 2.2.2 on 2019-06-30 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190630_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['-favorite_at']},
        ),
    ]