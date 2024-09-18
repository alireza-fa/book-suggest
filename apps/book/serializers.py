from rest_framework import serializers

from apps.book.models import Book, Author, Genre, BookReview
from apps.user.serializers import UserInfoSerializer


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "name")


class BookListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(method_name="get_author")
    genre = serializers.SerializerMethodField(method_name="get_genre")

    class Meta:
        model = Book
        fields = ("id", "title", "author", "genre")

    def get_author(self, obj):
        return AuthorSerializer(instance=obj.author).data

    def get_genre(self, obj):
        return GenreSerializer(instance=obj.genre).data


class BookReviewAddSerializer(serializers.ModelSerializer):
    # I don't like data sanitization that need to check a book in db exist or note, do it in serializers
    # So I get from client book id and check book is exist in services
    book_id = serializers.IntegerField()

    class Meta:
        model = BookReview
        fields = ("book_id", "rate")


class BookReviewDetailSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField(method_name="get_book")
    user = serializers.SerializerMethodField(method_name="get_user")

    class Meta:
        model = BookReview
        fields = ("id", "book", "rate", "user")

    def get_book(self, obj):
        return BookListSerializer(instance=obj.book).data

    def get_user(self, obj):
        return UserInfoSerializer(instance=obj.user).data
