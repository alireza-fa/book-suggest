from django.contrib import admin

from .models import Book, BookReview


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    pass
