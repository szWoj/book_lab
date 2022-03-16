from flask import Flask, render_template, request, redirect, Blueprint

from repositories import author_repository, book_repository

from models.author import Author
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', books=books)

@books_blueprint.route('/books/<id>/delete', methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

@books_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template('books/new.html', authors=authors)

@books_blueprint.route('/books', methods = ["POST"])
def add_book():
    title = request.form["title"]
    author = author_repository.select(request.form["author"])
    book = Book(title, author)
    book_repository.save(book)
    return redirect('/books')