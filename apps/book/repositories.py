from apps.book.models import Book


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


def get_book_repository():
    return BookRepository()
