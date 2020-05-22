# Generated by Django 2.2.12 on 2020-05-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(blank=True, default='', upload_to='app/images/movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]