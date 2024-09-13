

from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books: list[Book] = []
        self.__users: list[User] = []
        self.__checked_out_books: list[Book] = []
        self.__checked_in_books: list[Book] = []

    # Getters
    def get_books(self) -> list[Book]:
        return self.__books

    def get_users(self) -> list[User]:
        return self.__users

    def get_checked_out_books(self) -> list[Book]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list[Book]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        add: Book = Book(isbn, title, author)
        if add not in self.__books:
            self.__books.append(add)

    # 1.2 List All Books
    def list_all_books(self):
        for libro in self.__books:
            print(libro)

    # 2.1 Check out book

    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        for libro in self.__books:
            if libro.get_isbn() == isbn:
                if libro.is_available() == False:
                    return f"Book {isbn} is not available"
                else:
                    libro.set_available(False)
                    self.__checked_out_books.append(libro)
                    for user in self.__users:
                        if user.get_dni() == dni:
                            user.increment_checkouts()
                            return f"User {dni} checked out book {isbn}"
        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # 2.2 Check in book
    def check_in_book(self, isbn:str, dni:int, returned_date:str) -> str:
        for libro in self.__books:
            if libro.get_isbn() == isbn:
                if libro.is_available() == False:
                    libro.set_available(True)
                    self.__checked_in_books.append(libro)
                    for user in self.__users:
                        if user.get_dni() == dni:
                            user.increment_checkins()
                            self.__checked_out_books.remove(libro)
                            return f"Book {isbn} checked in by user {dni}"
        return f"Book {isbn} is not available or already checked in"

    # Utils
    def add_user(self, dni: int, name: str) -> None:
        self.__users.append(User(dni, name))


a = Book("9780743273565", "The Great Gatsby", "Fitzgerald")
print(a)