from models.author import Author
from models.book import Book

from repositories import author_repository, book_repository

author_1 = Author('Mark Smith')
author_repository.save(author_1)