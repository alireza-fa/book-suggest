from django.urls import path

from apps.book.views import BookListView, BookSuggestView, BookReviewAddView, BookReviewUpdateView, BookReviewDeleteView

app_name = "book"

urlpatterns = [
    # we can use book list api with search query parameters like(genre, title, author) instead writing two apis
    path("search/", BookListView.as_view(), name="book-list"),
    path("suggest/", BookSuggestView.as_view(), name="book-suggest"),
    # also we can use one view for all three below action, but I like every view write and do for single responsibility
    path("review/add/", BookReviewAddView.as_view(), name="book-review-add"),
    path("review/update/", BookReviewUpdateView.as_view(), name="book-review-update"),
    path("review/delete/", BookReviewDeleteView.as_view(), name="book-review-delete"),
]
