from rest_framework import serializers

from apps.book.models import Book, Author, Genre


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
        fields = ("title", "author", "genre")

    def get_author(self, obj):
        return AuthorSerializer(instance=obj.author).data

    def get_genre(self, obj):
        return GenreSerializer(instance=obj.genre).data
