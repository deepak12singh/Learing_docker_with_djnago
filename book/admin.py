from django.contrib import admin

# Register your models here.
from .models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'pages', 'language')
    search_fields = ('title', 'author', 'isbn', 'language')
    list_filter = ('published_date', 'language')