class Book:
    def __init__(self, title, author, publication_year):
        # (b) Private data attributes
        self._title = title
        self._author = author
        self._publication_year = publication_year

    # (c) Accessors (getters) and Mutators (setters)
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def get_publication_year(self):
        return self._publication_year

    def set_publication_year(self, publication_year):
        self._publication_year = publication_year

    # (d) __str__ method
    def __str__(self):
        return f"Book Title: {self._title}, Author: {self._author}, Publication Year: {self._publication_year}"

# (e) Create an object called bookOne and pass in arguments
bookOne = Book("The Catcher in the Rye", "J.D. Salinger", 1951)

# (f) Change at least two attributes and print new values using accessors
print("Original state of bookOne:")
print(bookOne)

# Change attributes using mutators
bookOne.set_title("Blossoms of the savannah")
bookOne.set_publication_year(2016)

# Print new values using accessors
print("\nUpdated state of bookOne:")
print(f"Title: {bookOne.get_title()}")
print(f"Author: {bookOne.get_author()}")
print(f"Publication Year: {bookOne.get_publication_year()}")
