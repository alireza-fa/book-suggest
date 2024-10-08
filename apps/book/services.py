from functools import cache
from abc import ABC, abstractmethod

from apps.book.repositories import get_book_repository
from apps.common import codes
from pkg.rich_error.error import RichError


class Repository(ABC):

    @abstractmethod
    def search(self, search):
        pass

    @abstractmethod
    def check_book_is_exist_by_id(self, book_id: int) -> bool:
        pass

    @abstractmethod
    def check_book_review_is_exist(self, user_id: int, book_id: int):
        pass

    @abstractmethod
    def add_book_review(self, user_id: int, book_id: int, rate: int):
        pass

    @abstractmethod
    def update_book_review(self, user_id: int, book_id: int, rate: int):
        pass

    @abstractmethod
    def delete_book_review(self, user_id: int, book_id: int):
        pass

    @abstractmethod
    def check_user_add_review_book(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_suggest_books(self, user_id: int):
        pass


class BookService:
    Op = "book.services.BookService."

    def __init__(self, repo: Repository):
        self.repo = repo

    def search(self, search):
        return self.repo.search(search=search)

    def add_book_review(self, user_id: int, book_id: int, rate: int):
        op = self.Op + "add_book_review"

        if not self.repo.check_book_is_exist_by_id(book_id=book_id):
            raise RichError(op).set_code(codes.BOOK_NOT_FOUND)

        if self.repo.check_book_review_is_exist(user_id=user_id, book_id=book_id):
            raise RichError(op).set_code(codes.BOOK_REVIEW_CONFLICT)

        return self.repo.add_book_review(user_id=user_id, book_id=book_id, rate=rate)

    def update_book_review(self, user_id: int, book_id: int, rate: int):
        op = self.Op + "update_book_review"

        if not self.repo.check_book_review_is_exist(user_id=user_id, book_id=book_id):
            raise RichError(op).set_code(codes.BOOK_REVIEW_NOT_FOUND)

        self.repo.update_book_review(user_id=user_id, book_id=book_id, rate=rate)

    def delete_book_review(self, user_id: int, book_id: int):
        op = self.Op + "delete_book_review"

        if not self.repo.check_book_review_is_exist(user_id=user_id, book_id=book_id):
            raise RichError(op).set_code(codes.BOOK_REVIEW_NOT_FOUND)

        self.repo.delete_book_review(user_id=user_id, book_id=book_id)

    def get_suggest_books(self, user_id: int):
        op = self.Op + "get_suggest_books"

        if not self.repo.check_user_add_review_book(user_id=user_id):
            raise RichError(op).set_code(codes.SUGGEST_BOOKS_NOT_FOUND)

        return self.repo.get_user_suggest_books(user_id=user_id)


@cache
def get_book_service():
    return BookService(repo=get_book_repository())
