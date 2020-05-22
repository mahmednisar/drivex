"""
Definition of urls for drive.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('books/', views.books, name='books'),
    path('books/view/<int:bookid>', views.booksview, name='booksview'),
    path('movies/view/<int:movieid>', views.movieview, name='movieview'),
    path('books/cprogramming/', views.cprogramming, name='ProgrammingwithC'),
    path('books/cpp/', views.cpp, name='ProgrammingwithC++'),
    path('books/csharp/', views.csharp, name='ProgrammingwithC#'),
    path('books/java/', views.java, name='ProgrammingwithJava'),
    path('books/python', views.python, name='ProgrammingwithPython'),
    path('books/compititive', views.compititive, name='CompititiveBooks'),
    path('books/comics', views.comics, name='ComicsBooks'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('tutorials/view/<int:tutorialid>', views.tutorialview, name='tutorialview'),
    path('softwares/view/<int:softwareid>', views.softwareview, name='softwareview'),
    path('softwares/', views.softwares, name='softwares'),
    path('movies/', views.movies, name='movies'),
    path('login/',
         LoginView.as_view(template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('superuser/', admin.site.urls),] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
