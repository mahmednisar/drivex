# Generated by Django 2.2.12 on 2020-05-22 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_series'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='movie_description',
            new_name='series_description',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='movie_image',
            new_name='series_image',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='movie_language',
            new_name='series_language',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='movie_url',
            new_name='series_url',
        ),
    ]