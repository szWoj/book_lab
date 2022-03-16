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