# schema.py

import strawberry
from typing import List, Optional
from models import Author, Book, authors, books

@strawberry.type
class AuthorType:
    id: int
    name: str

@strawberry.type
class BookType:
    id: int
    title: str
    author: AuthorType

    @strawberry.field
    def author(self) -> AuthorType:
        return next(a for a in authors if a.id == self.author_id)

    author_id: int  # usado internamente para resolver el autor

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[BookType]:
        return books

    @strawberry.field
    def authors(self) -> List[AuthorType]:
        return authors

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book(self, title: str, author_id: int) -> BookType:
        book = Book(id=len(books)+1, title=title, author_id=author_id)
        books.append(book)
        return book

schema = strawberry.Schema(query=Query, mutation=Mutation)
