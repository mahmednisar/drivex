"""
Definition of models.
"""

from django.db import models
from multiselectfield import MultiSelectField


class Genere(models.Model):
    genere_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)
   
    def __str__(self):
        return self.genere_name
 

class Quality(models.Model):
    quality_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)
   
    def __str__(self):
        return self.quality_name

class Rating(models.Model):
    rating_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)
   
    def __str__(self):
        return self.rating_name

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)
   
    def __str__(self):
        return self.category_name
 
class Language(models.Model):
    language_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)
   
    def __str__(self):
        return self.language_name
 

class Year(models.Model):
    year_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)
   
    def __str__(self):
        return self.year_name
 


class Book_Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)
   
    def __str__(self):
        return self.category_name
    

class Book_Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category=  models.ForeignKey(Book_Category, related_name='category',default=None, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.subcategory_name


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_category = models.ForeignKey(Book_Category, related_name='book_category',default=None, on_delete=models.CASCADE)
    book_subcategory = models.ForeignKey(Book_Subcategory, related_name='book_subcategory',default=None, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True)
    book_description = models.TextField()
    book_author = models.CharField(max_length=100, default="",blank=True)
    book_url = models.CharField(max_length=500,blank=True)
    #book_publish = models.IntegerField(_('year'), default=current_year)
    book_publish = models.DateField(blank=True)
    book_image = models.ImageField(upload_to="app/images/books", default="",blank=True)

    def __str__(self):
        return self.book_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    movie_genere = models.ForeignKey(Genere, related_name='movie_genere',default=None, on_delete=models.CASCADE)
    movie_year = models.ForeignKey(Year, related_name='movie_year',default=None, on_delete=models.CASCADE)
    movie_quality = models.ForeignKey(Quality, related_name='movie_quality',default=None, on_delete=models.CASCADE)
    movie_rating = models.ForeignKey(Rating, related_name='movie_rating',default=None, on_delete=models.CASCADE)
    movie_category =  models.ForeignKey(Category, related_name='movie_category',default=None, on_delete=models.CASCADE)
    movie_language =  models.ForeignKey(Language, related_name='movie_language',default=None, on_delete=models.CASCADE)
    movie_description =models.TextField(blank=True)
    movie_url = models.CharField(max_length=500,blank=True)
    movie_image = models.ImageField(upload_to="app/images/movie", default="",blank=True)

    def __str__(self):
        return self.movie_name

class Series(models.Model):
    series_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    series_genere =  models.ForeignKey(Genere, related_name='series_genere',default=None, on_delete=models.CASCADE)
    series_year =  models.ForeignKey(Year, related_name='series_year',default=None, on_delete=models.CASCADE)
    series_rating =   models.ForeignKey(Rating, related_name='series_rating',default=None, on_delete=models.CASCADE)
    series_language =   models.ForeignKey(Language, related_name='series_language',default=None, on_delete=models.CASCADE)
    series_description =models.TextField(blank=True)
    series_url = models.CharField(max_length=500,blank=True)
    series_image = models.ImageField(upload_to="app/images/series", default="",blank=True)

    def __str__(self):
        return self.series_name



class Tutorial_Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField( blank=True)
   
    def __str__(self):
        return self.category_name
    

class Tutorial_Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category=  models.ForeignKey(Tutorial_Category, related_name='category',default=None, on_delete=models.CASCADE)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.subcategory_name
 

class Tutorial(models.Model):
    tutorial_name = models.CharField(max_length=100)
    tutorial_category = models.ForeignKey(Tutorial_Category, related_name='tutoral_category',default=None, on_delete=models.CASCADE)
    tutorial_subcategory = models.ForeignKey(Tutorial_Subcategory, related_name='tutorial_subcategory',default=None, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True)
    tutorial_description =  models.TextField(blank=True)
    tutorial_rating =  models.ForeignKey(Rating, related_name='tutorial_rating',default=None, on_delete=models.CASCADE)
    tutorial_url =  models.CharField(max_length=500, blank=True)
    tutorial_image = models.ImageField(upload_to="app/images/tutorial", default="",blank=True)

    def __str__(self):
        return self.tutorial_name



class Software_Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.category_name
    

class Software_Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category=  models.ForeignKey(Software_Category, related_name='category',default=None, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.subcategory_name
 

class Software(models.Model):
    software_name = models.CharField(max_length=100)
    software_category = models.ForeignKey(Software_Category, related_name='software_category',default=None, on_delete=models.CASCADE)
    software_subcategory = models.ForeignKey(Software_Subcategory, related_name='software_subcategory',default=None, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, blank=True)
    software_description =  models.TextField(blank=True)
    software_rating =   models.ForeignKey(Rating, related_name='software_rating',default=None, on_delete=models.CASCADE)
    software_url =  models.CharField(max_length=500, blank=True)
    software_image = models.ImageField(upload_to="app/images/software", default="",blank=True)

    def __str__(self):
        return self.software_name