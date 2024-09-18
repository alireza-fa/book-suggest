from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

User = get_user_model()


class Author(BaseModel):
    name = models.CharField(max_length=64, verbose_name=_("name"), db_index=True, unique=True)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name


class Genre(BaseModel):
    name = models.CharField(max_length=64, verbose_name=_("name"), unique=True, db_index=True)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genres")

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=191, verbose_name=_("title"), db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books", verbose_name=_("author"))
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="genres", verbose_name=_("gemre"))

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return f"title: {self.title} - {self.author} - {self.genre}"


class BookReviewEnum:
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    ALL_RATE = (ONE, TWO, THREE, FOUR, FIVE)

    RATE_CHOICES = (
        (ONE, _("one")),
        (TWO, _("two")),
        (THREE, _("three")),
        (FOUR, _("four")),
        (FIVE, _("five")),
    )


class BookReview(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews",
                             verbose_name=_("book"), db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews",
                             verbose_name=_("user"), db_index=True)
    rate = models.PositiveSmallIntegerField(choices=BookReviewEnum.RATE_CHOICES, verbose_name=_("rate"))

    class Meta:
        verbose_name = _("Book Review")
        verbose_name_plural = _("Book Reviews")
