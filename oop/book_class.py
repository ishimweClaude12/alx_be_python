class Book:
    """A class representing a book with magic methods."""

    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation to recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
