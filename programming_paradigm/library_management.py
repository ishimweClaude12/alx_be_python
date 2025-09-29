class Book:
    """Represents a single book in the library."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # wasn't checked out

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Readable representation of a book."""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a collection of books in the library."""

    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book: Book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # not found or already checked out

    def return_book(self, title: str):
        """Return a book by title (make it available again)."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # not found or wasn't checked out

    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
