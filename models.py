# models.py

class Author:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class Book:
    def __init__(self, id: int, title: str, author_id: int):
        self.id = id
        self.title = title
        self.author_id = author_id

# Datos de ejemplo
authors = [
    Author(1, "J.K. Rowling"),
    Author(2, "J.R.R. Tolkien")
]

books = [
    Book(1, "Harry Potter and the Philosopher's Stone", 1),
    Book(2, "The Hobbit", 2)
]
