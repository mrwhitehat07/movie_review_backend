# Generated by Django 4.0 on 2022-02-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movie_poster_alter_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
