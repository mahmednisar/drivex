from .models import  Book, Movie, Tutorial,Tutorial_Category, Tutorial_Subcategory, Book_Category, Book_Subcategory, Software_Category, Software_Subcategory, Software, Series, Genere, Quality, Rating, Category, Language, Year


def add_variable_to_context(request):
    bookscategory= Book_Subcategory.objects.all()
    tutscategory= Tutorial_Subcategory.objects.all()
    softwarescategory= Software_Category.objects.all()
    genere= Genere.objects.all()
    quality=Quality.objects.all()
    rating=Rating.objects.all()
    category= Category.objects.all()
    language= Language.objects.all()
    year=Year.objects.all()
    return {
        'bookscategory':bookscategory, 'tutscategory':tutscategory, 'softwarescategory':softwarescategory,'genere':genere,'quality':quality,'rating':rating,'category':category, 'language':language, 'year':year
    }