from django.contrib import  admin
from .models import Book, Movie, Tutorial,Tutorial_Category, Tutorial_Subcategory, Book_Category,Book_Subcategory,Software_Category,Software_Subcategory, Software


admin.site.site_header = 'Drive Links (Admin Pannel)'
admin.site.site_title = 'Drive Links (Admin Pannel)'

class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'movie_genere', 'movie_year', 'movie_quality', 'movie_rating', 'movie_category', 'movie_language']
    list_filter = ['movie_genere', 'movie_quality',  'movie_category', 'movie_language',]
    list_editable = ['movie_rating']

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'book_category', 'book_subcategory', 'book_author', 'book_publish']
    list_filter = ['book_category', 'book_subcategory']

class TutorialAdmin(admin.ModelAdmin):
    list_display = ['tutorial_name', 'tutorial_category', 'tutorial_subcategory', 'tutorial_rating']
    list_filter = ['tutorial_category', 'tutorial_subcategory']
    list_editable = ['tutorial_rating']

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ['software_name', 'software_category', 'software_subcategory', 'software_rating']
    list_filter = ['software_category', 'software_subcategory']
    list_editable = ['software_rating']

class Book_SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name', 'category']
    list_filter = ['category']
    list_editable = ['category']

class Software_SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name', 'category']
    list_filter = ['category']
    list_editable = ['category']

class Tutorial_SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_name', 'category']
    list_filter = ['category']
    list_editable = ['category']


admin.site.register(Book,BookAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Tutorial_Category)
admin.site.register(Tutorial_Subcategory,Tutorial_SubcategoryAdmin)
admin.site.register(Book_Category)
admin.site.register(Book_Subcategory,Book_SubcategoryAdmin)
admin.site.register(Software_Category)
admin.site.register(Software_Subcategory,Software_SubcategoryAdmin)
admin.site.register(Software,SoftwareAdmin)


