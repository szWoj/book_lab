from models.author import Author
from models.book import Book

from repositories import author_repository, book_repository

author_1 = Author('Mark Smith')
author_2 = Author('Ernest Hemingway')
author_repository.save(author_1)
author_repository.save(author_2)
book_1 = Book("My first book", author_1)
book_2 = Book("My second book", author_2)
book_repository.save(book_1)
book_repository.save(book_2)

book_repository.delete(book_1.id)
all_books = book_repository.select_all()
for book in all_books:
    print(book.__dict__)


# print(author_repository.select(author_1.id).__dict__)