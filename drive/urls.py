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
    path('series/view/<int:seriesid>', views.seriesview, name='seriesview'),
    path('books/subcategory/<int:subcatid>', views.booksubcategory, name='booksubcategory'),
    path('books/category/<int:catid>', views.bookcategory, name='bookcategory'),
    path('tutorials/subcategory/<int:subcatid>', views.tutsubcategory, name='tutsubcategory'),
    path('tutorials/category/<int:catid>', views.tutcategory, name='tutcategory'),
    path('softwares/subcategory/<int:subcatid>', views.softwaresubcategory, name='softwaresubcategory'),
    path('softwares/category/<int:catid>', views.softwarecategory, name='softwarecategory'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('tutorials/view/<int:tutorialid>', views.tutorialview, name='tutorialview'),
    path('softwares/view/<int:softwareid>', views.softwareview, name='softwareview'),
    path('softwares/', views.softwares, name='softwares'),
    path('movies/', views.movies, name='movies'),
    path('series/', views.series, name='series'),
    path('series/genere/<int:id>', views.seriesgenere, name='seriesgenere'),
    path('series/year/<int:id>', views.seriesyear, name='seriesyear'),
    path('series/rating/<int:id>', views.seriesrating, name='seriesrating'),
    path('movies/genere/<int:id>', views.moviegenere, name='moviegenere'),
    path('movies/year/<int:id>', views.movieyear, name='movieyear'),
    path('movies/rating/<int:id>', views.movierating, name='movierating'),
    path('movies/quality/<int:id>', views.moviequality, name='moviequality'),
    path('movies/category/<int:id>', views.moviecategory, name='moviecategory'),
    path('movies/language/<int:id>', views.movielanguage, name='movielanguage'),
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
