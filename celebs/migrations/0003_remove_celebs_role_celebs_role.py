# Generated by Django 4.0 on 2022-01-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebs', '0002_alter_celebs_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebs',
            name='role',
        ),
        migrations.AddField(
            model_name='celebs',
            name='role',
            field=models.ManyToManyField(to='celebs.Role'),
        ),
    ]