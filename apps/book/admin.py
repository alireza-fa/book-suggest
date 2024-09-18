from django.contrib import admin

from .models import Book, BookReview, Author, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
