from django.db.models import Avg, Count

from apps.book.models import Book, BookReview


class BookRepository:
    Model = Book

    def search(self, search):
        queryset = self.Model.objects.select_related("author", "genre").all()
        # we can filter with title, author, genre, etc.
        # TODO - using slug instead id?!
        # search example: /search/?page_size=1&genre=5&genre=2&author=4&title=romeo

        if search.get("genre"):
            queryset = queryset.filter(genre__id__in=search.getlist("genre"))

        if search.get("author"):
            queryset = queryset.filter(author_id__in=search.getlist("author"))

        if search.get("title"):
            queryset = queryset.filter(title__icontains=search.get("title"))

        return queryset

    def check_book_is_exist_by_id(self, book_id: int) -> bool:
        return self.Model.objects.only("id").filter(id=book_id).exists()

    def check_book_review_is_exist(self, user_id: int, book_id: int):
        return BookReview.objects.only("id").filter(user_id=user_id, book_id=book_id).exists()

    def add_book_review(self, user_id: int, book_id: int, rate: int):
        return BookReview.objects.create(
            book_id=book_id,
            user_id=user_id,
            rate=rate
        )

    def update_book_review(self, user_id: int, book_id: int, rate: int):
        return BookReview.objects.filter(user_id=user_id, book_id=book_id).update(rate=rate)

    def delete_book_review(self, user_id: int, book_id: int):
        return BookReview.objects.filter(user_id=user_id, book_id=book_id).delete()

    def check_user_add_review_book(self, user_id: int) -> bool:
        return BookReview.objects.only("id").filter(user_id=user_id).exists()

    @staticmethod
    def get_user_book_review_genres(user_id: int):
        return BookReview.objects.filter(user_id=user_id).values_list("book__genre__id", flat=True)

    def get_user_suggest_books(self, user_id: int):
        user_reviews = BookReview.objects.filter(user_id=user_id)

        genres_rated = (
            user_reviews.values('book__genre').annotate(
                avg_rate=Avg('rate'),
                count=Count('book__genre')
            ).order_by('-avg_rate', '-count')
        )

        top_genres = [genre['book__genre'] for genre in genres_rated[:3]]

        recommended_books = Book.objects.filter(
            genre__in=top_genres
        ).exclude(
            id__in=user_reviews.values_list('book_id', flat=True)
        ).distinct()

        return recommended_books


def get_book_repository():
    return BookRepository()
