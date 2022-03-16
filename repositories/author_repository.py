from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = (%s)"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        author = Author(result['name'], id)
    return author