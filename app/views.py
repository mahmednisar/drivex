"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Book, Movie, Tutorial,Tutorial_Category, Tutorial_Subcategory, Book_Category, Book_Subcategory, Software_Category, Software_Subcategory, Software, Series, Genere, Quality, Rating, Category, Language, Year
from django.http import HttpResponse
from django.core.paginator import Paginator

def home(request):
    return render(request,'app/index.html')

def contact(request):
    return render(request,'app/contact.html')

def about(request):
    return render(request,'app/about.html')

def books(request):
    books= Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'All Books', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def booksview(request, bookid):
    books= Book.objects.filter(id=bookid)
    category= Book_Subcategory.objects.all()
    params ={'heading':'Category','title':'Details', 'page_obj': books, 'category':category}
    return render(request,'app/bookview.html', params)

def movies(request):
    movie= Movie.objects.all()
    paginator = Paginator(movie, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'All Movies', 'page_obj': page_obj}
    return render(request,'app/movies.html', params)

def movieview(request, movieid):
    movie= Movie.objects.filter(id=movieid)
    movie_genere = Genere.objects.all()
    movie_year = Year.objects.all()
    movie_category = Category.objects.all()
    params ={'heading':'Category','title':movie, 'page_obj': movie, 'movie_genere':movie_genere, 'movie_year':movie_year, 'movie_category':movie_category }
    return render(request,'app/movieview.html', params)

def series(request):
    series= Series.objects.all()
    paginator = Paginator(series, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'All Series', 'page_obj': page_obj}
    return render(request,'app/series.html', params)

def seriesview(request, seriesid):
    series= Series.objects.filter(id=seriesid)
    series_genere = Genere.objects.all()
    series_year = Year.objects.all()
    params ={'heading':'Category','title':Series, 'page_obj': series,'series_genere':series_genere,'series_year':series_year }
    return render(request,'app/seriesview.html', params)

def tutorials(request):
    tutorial= Tutorial.objects.all()
    paginator = Paginator(tutorial, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'All Tutorials', 'page_obj': page_obj}
    return render(request,'app/tutorials.html', params)

def tutorialview(request, tutorialid):
    tutorial= Tutorial.objects.filter(id=tutorialid)
    category= Tutorial_Subcategory.objects.all()
    params ={'heading':'Category','title':tutorial, 'page_obj': tutorial,'category':category }
    return render(request,'app/tutorialview.html', params)

def softwares(request):
    softwares= Software.objects.all()
    paginator = Paginator(softwares, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'All Softwares', 'page_obj': page_obj}
    return render(request,'app/softwares.html', params)

def softwareview(request, softwareid):
    softwares= Software.objects.filter(id=softwareid)
    category= Software_Subcategory.objects.all()
    params ={'heading':'Category','title':softwares, 'page_obj': softwares,'category':category }
    return render(request,'app/softwareview.html', params)

def booksubcategory(request, subcatid):
    books= Book.objects.filter(book_subcategory=subcatid)
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Books',  'page_obj': page_obj}
    return render(request,'app/books.html', params)

def bookcategory(request, catid):
    books= Book.objects.filter(book_subcategory=catid)
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Books', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def tutsubcategory(request, subcatid):
    tutorial= Book.objects.filter(tutorial_subcategory=subcatid)
    paginator = Paginator(tutorial, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Tutorials', 'page_obj': page_obj}
    return render(request,'app/tutorials.html', params)

def tutcategory(request, catid):
    tutorial= Book.objects.filter(tutorial_category=catid)
    paginator = Paginator(tutorial, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Tutorials', 'page_obj': page_obj}
    return render(request,'app/tutorials.html', params)

def softwaresubcategory(request, subcatid):
    software= Software.objects.filter(software_subcategory=subcatid)
    paginator = Paginator(software, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Softwares', 'page_obj': page_obj}
    return render(request,'app/softwares.html', params)

def softwarecategory(request, catid):
    software= Software.objects.filter(software_category=catid)
    paginator = Paginator(software, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Software', 'page_obj': page_obj}
    return render(request,'app/tutorials.html', params)

def seriesgenere(request, id):
    series= Series.objects.filter(series_genere=id)
    paginator = Paginator(series, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Series', 'page_obj': page_obj}
    return render(request,'app/series.html', params)

def seriesyear(request, id):
    series= Series.objects.filter(series_year=id)
    paginator = Paginator(series, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Series', 'page_obj': page_obj}
    return render(request,'app/series.html', params)

def seriesrating(request, id):
    series= Series.objects.filter(series_rating=id)
    paginator = Paginator(series, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Series', 'page_obj': page_obj}
    return render(request,'app/series.html', params)

def moviegenere(request, id):
    movie= Movie.objects.filter(movie_genere=id)
    paginator = Paginator(movie, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Movies', 'page_obj': page_obj}
    return render(request,'app/movies.html', params)

def movieyear(request, id):
    movie= Movie.objects.filter(movie_year=id)
    paginator = Paginator(movie, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Movies', 'page_obj': page_obj}
    return render(request,'app/movies.html', params)

def movierating(request, id):
    movie= Movie.objects.filter(movie_rating=id)
    paginator = Paginator(movie, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Movies', 'page_obj': page_obj}
    return render(request,'app/movies.html', params)

def moviequality(request, id):
    movie= Movie.objects.filter(movie_quality=id)
    paginator = Paginator(movie, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Movies', 'page_obj': page_obj}
    return render(request,'app/movies.html', params)

def moviecategory(request, id):
    movie= Movie.objects.filter(movie_category=id)
    paginator = Paginator(movie, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Movies', 'page_obj': page_obj}
    return render(request,'app/movies.html', params)

def movielanguage(request, id):
    movie= Movie.objects.filter(movie_language=id)
    paginator = Paginator(movie, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'title':'Movies', 'page_obj': page_obj}
    return render(request,'app/movies.html', params)
