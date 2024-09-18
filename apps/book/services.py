from functools import cache
from abc import ABC, abstractmethod

from apps.book.repositories import get_book_repository


class Repository(ABC):

    @abstractmethod
    def search(self, search):
        pass


class BookService:

    def __init__(self, repo: Repository):
        self.repo = repo

    def search(self, search):
        return self.repo.search(search=search)


@cache
def get_book_service():
    return BookService(repo=get_book_repository())
