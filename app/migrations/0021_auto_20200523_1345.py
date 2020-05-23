# Generated by Django 2.2.12 on 2020-05-23 08:15

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200523_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_url', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genere_name', models.CharField(max_length=100)),
                ('Genere_url', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=100)),
                ('language_url', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_name', models.CharField(max_length=100)),
                ('quality_url', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_name', models.CharField(max_length=100)),
                ('rating_url', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_name', models.CharField(max_length=100)),
                ('year_url', models.CharField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='software',
            name='software_rating',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_rating',
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie_category', to='app.Category'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_genere',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie_genere', to='app.Genere')),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_language',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie_language', to='app.Language'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_quality',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie_quality', to='app.Quality'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_rating',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie_rating', to='app.Rating'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_year',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='movie_year', to='app.Year'),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_genere',
            field=multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='series_genere', to='app.Genere')),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_language',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='series_language', to='app.Language'),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_rating',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='series_rating', to='app.Rating'),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_year',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='series_year', to='app.Year'),
        ),
    ]
