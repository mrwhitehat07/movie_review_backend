# Generated by Django 4.0 on 2022-01-10 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_genre_remove_movie_genre_alter_movie_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
    ]