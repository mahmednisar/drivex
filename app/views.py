"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Book, Movie, Tutorial, Software
from django.http import HttpResponse
from django.core.paginator import Paginator

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'year':datetime.now().year,
        }
    )

def books(request):
    books= Book.objects.all()
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'All Books', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def booksview(request, bookid):
    books= Book.objects.filter(id=bookid)
    params ={'heading':'Category','title':'Details', 'page_obj': books}
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
    params ={'heading':'Category','title':movie, 'page_obj': movie }
    return render(request,'app/movieview.html', params)

def tutorials(request):
    tutorial= Tutorial.objects.all()
    paginator = Paginator(tutorial, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'All Tutorials', 'page_obj': page_obj}
    return render(request,'app/tutorials.html', params)

def tutorialview(request, tutorialid):
    tutorial= Tutorial.objects.filter(id=tutorialid)
    params ={'heading':'Category','title':tutorial, 'page_obj': tutorial }
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
    params ={'heading':'Category','title':softwares, 'page_obj': softwares }
    return render(request,'app/softwareview.html', params)

def cprogramming(request):
    books= Book.objects.filter(book_category='c')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'Programming with C', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def cpp(request):
    books= Book.objects.filter(book_category='cpp')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'Programming with C++', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def java(request):
    books= Book.objects.filter(book_category='java')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'Programming with Java', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def csharp(request):
    books= Book.objects.filter(book_category='csharp')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'C# Programming', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def python(request):
    books= Book.objects.filter(book_category='python')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'Python', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def compititive(request):
    books= Book.objects.filter(book_category='compitition')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'Compitition', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

def comics(request):
    books= Book.objects.filter(book_category='comics')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params ={'heading':'Category','title':'Comics', 'page_obj': page_obj}
    return render(request,'app/books.html', params)

