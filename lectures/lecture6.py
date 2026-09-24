"""Lecture 6 notes on using objects"""

import pytest


class Book:
    def __init__(self, checked_out: bool, title: str, author: str, wordcount: int):
        self.checked_out: bool = checked_out
        self.title: str = title
        self.author: str = author
        self.wordcount: int = wordcount
    
    def __str__(self) -> str:
        return self.title + ' written by ' + self.author

    def check_out(self, check_out: bool) -> None:
        """Checks if the current book is checked in and allows user to check it out"""
        if check_out and not self.checked_out:
            self.checked_out = True
        else:
            self.checked_out = False

    def compare_book_length(self, wordcount: int) -> bool:
        """Compares two books by length and returns True if they are the same length"""
        if self.wordcount > wordcount:
            print()
            return False


book: Book = Book(False, "How to Code", "Linus Torvald", 256)


@pytest.fixture(name="book")
def test_check_out() -> None:
    """Tests the checkout function of the Book class"""
    book.check_out(True)
    assert book.checked_out


"""
Variables hold references to objects that are stored somewhere in memory
Multiple variables can be aliases of the same object which is how equality checks are carried out it checks if both are aliases of the same object
"""

original: list[int] = [1, 4, 7]

alias: list[int] = original
copy: list[int] = original.copy()

"""
Every class has a __str__() method, when you print an object thats what it uses
"""

print(book)
