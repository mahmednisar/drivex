"""
Definition of models.
"""

from django.db import models
from multiselectfield import MultiSelectField

CATEGORIES = (  
    ( 'c','Programming With C'),
    ( 'cpp','Programming With C++'),
    ( 'csharp','Programming With C#'),
    ( 'java','Programming With Java'),
    ( 'python','Programming With Python'),
    ( 'compitition','Compitition'),
    ( 'comics','Comics'),
)

GENERE = (
    ( 'Action','Action'),
    ( 'Adventure','Adventure'),
    ( 'Comedy','Comedy'),
    ( 'Crime','Crime'),
    ( 'Drama','Drama'),
    ( 'Epics','Epics'),
    ( 'Horror','Horror'),
    ( 'Musicals','Musicals (Dance)'),
    ( 'Science','Science Fiction'),
    ( 'War','War (Anti-War)'),
)

QUALITY = (
    ( '480p','480p'),
    ( '720p','720p'),
    ( '1080p','1080p'),
    ( '4K','4K'),
)

RATING = (
    ( '1','1'),
    ( '2','2'),
    ( '3','3'),
    ( '4','4'),
    ( '5','5'),
    ( '6','7'),
    ( '8','8'),
    ( '9','9'),
    ( '10','10'),
)

MCATEGORY = (
     ( 'Bollywood','Bollywood'),
     ( 'Hollywood','Hollywood'),
     ( 'South','South'),
)
LANGUAGE = (
    ( 'English','English'),
    ( 'Hindi','Hindi'),
    ( 'Punjabi','Punjabi'),
    ( 'DualAudio','Dual Audio'),
    ( 'MultiAudio','Multi Audio'),
   
)


class Book_Category(models.Model):
    category_name = models.CharField(max_length=100)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.category_name
    

class Book_Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category=  models.ForeignKey(Book_Category, related_name='category',default=None, on_delete=models.CASCADE)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.subcategory_name


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_category = models.ForeignKey(Book_Category, related_name='book_category',default=None, on_delete=models.CASCADE)
    book_subcategory = models.ForeignKey(Book_Subcategory, related_name='book_subcategory',default=None, on_delete=models.CASCADE)
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
    movie_genere = MultiSelectField(choices=GENERE)
    movie_year = models.DateField(blank=True)
    movie_quality =  models.CharField(max_length=50, choices=QUALITY)
    movie_rating =  models.CharField(max_length=50, choices=RATING)
    movie_category =  models.CharField(max_length=50, choices=MCATEGORY)
    movie_language =  models.CharField(max_length=50, choices=LANGUAGE)
    movie_description =models.TextField(blank=True)
    movie_url = models.CharField(max_length=500,blank=True)
    movie_image = models.ImageField(upload_to="app/images/movie", default="",blank=True)

    def __str__(self):
        return self.movie_name



class Tutorial_Category(models.Model):
    category_name = models.CharField(max_length=100)
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
    tutorial_description =  models.TextField(blank=True)
    tutorial_rating =  models.CharField(max_length=50, choices=RATING)
    tutorial_url =  models.CharField(max_length=500, blank=True)
    tutorial_image = models.ImageField(upload_to="app/images/tutorial", default="",blank=True)

    def __str__(self):
        return self.tutorial_name



class Software_Category(models.Model):
    category_name = models.CharField(max_length=100)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.category_name
    

class Software_Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category=  models.ForeignKey(Software_Category, related_name='category',default=None, on_delete=models.CASCADE)
    description =  models.TextField(blank=True)

    def __str__(self):
        return self.subcategory_name
 

class Software(models.Model):
    software_name = models.CharField(max_length=100)
    software_category = models.ForeignKey(Software_Category, related_name='software_category',default=None, on_delete=models.CASCADE)
    software_subcategory = models.ForeignKey(Software_Subcategory, related_name='software_subcategory',default=None, on_delete=models.CASCADE)
    software_description =  models.TextField(blank=True)
    software_rating =  models.CharField(max_length=50, choices=RATING, blank=True)
    software_url =  models.CharField(max_length=500, blank=True)
    software_image = models.ImageField(upload_to="app/images/software", default="",blank=True)

    def __str__(self):
        return self.software_name