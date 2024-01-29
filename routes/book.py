from flask import Blueprint, render_template, request

book = Blueprint("book", __name__)

BOOKS = [
  {"id": 1, "title": "The big book", "author": "Jhon Doe"},
  {"id": 2, "title": "Big apple", "author": "Maria"},
  {"id": 3, "title": "The tester", "author": "Tavares"},
]

@book.route("/")
def list_book():
  return render_template('table.html', books=BOOKS)

@book.route("/", methods=["POST"])
def insert_book():
  data = request.json
  new_book = {
    "id": len(BOOKS) + 1,
    "title": data.get('title'),
    "author": data.get('author')
  }
  BOOKS.append(new_book)
  return render_template('table.html', books=BOOKS)

@book.route('/new')
def form():
  return render_template('form.html')