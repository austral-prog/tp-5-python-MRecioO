class Book:
    def __init__(self, isbn: str, title: str, author: str, available: bool = True, checkout_num: int=0):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__available = available
        self.__checkout_num = checkout_num

    # Getters
    def get_isbn(self) -> str :
        return self.__isbn

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def is_available(self) -> bool:
        return self.__available

    def get_checkout_num(self) -> int:
        return self.__checkout_num

    # Setters
    def set_available(self, available: bool) -> None :
        self.__available = available

    def increment_checkout_num(self) -> None:
        self.__checkout_num +=   1

    # Utils
    def __str__(self) -> str:
        return f'ISBN: {self.__isbn}, Title: {self.__title}, Author: {self.__author}'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Book):
            return self.__isbn == other.__isbn
        return False

    def display_info(self):
        print([self.__isbn, self.__title, self.__author, self.__available, self.__checkout_num])


book: Book = Book("9780743273565", "The Great Gatsby", "Fitzgerald", )


book.display_info()
