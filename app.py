from graphql import Location
from api import app, db
from api import models
from api.models import Book, Author
from flask import jsonify, render_template, request

def create_author():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({
            'error':'Bad request',
            'message': 'name needs to be present'
        })
    new_author = Author(
        name=data['name'],
        location=data['location'],
        age=data['age'],
        gender=data['gender'],
        # books=data['books'] #how to update books
    )
    db.session.add(new_author)
    db.session.commit()
    return new_author.to_dict()

def create_book():
    data = request.get_json()
    if 'title' not in data:
        return jsonify({
            'error':'Bad request',
            'message': 'title needs to be present'
        })
    author=Author.query.filter_by(id=data['author']).first()
    if author == None:
        return jsonify({
            'error':'Bad request',
            'message': 'Author does not exist, create author first.'
        })
    new_book = Book(
        title=data['title'],
        genre=data['genre'],
        height=data['height'],
        publisher=data['publisher'],
        author=author
    )
    db.session.add(new_book)
    db.session.commit()
    return new_book.to_dict()
    
#____________________________________________________ endpoint definition _________________________________________

@app.route('/api/v1/books', methods=["POST", "GET", "DELETE"])
def all_books():
    if request.method == 'POST':
        return create_book()
    books = []
    all_books = Book.query.all()
    for item in all_books:
        books.append(item.to_dict())
    # return render_template("book_list.html", books=books)
    return jsonify(books)

@app.route('/api/v1/authors', methods=['GET', 'POST'])
def all_authors():
    if request.method == 'POST':
        return create_author()
    authors = []
    all_authors = Author.query.all()
    for item in all_authors:
        authors.append(item.to_dict())
    return jsonify(authors)
    # authors = jsonify(final_dict)
    # print('Authors', authors)
    # return render_template("author_list.html", authors=authors)



@app.route('/api/v1/books/<int:book_id>', methods=['GET', 'POST','DELETE'])
def single_book(book_id):
    book = Book.query.filter_by(id=book_id).first_or_404()
    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return{
            'success': 'Data deleted'
        }
    return jsonify(book.to_dict())
    # return render_template("book_detail.html", book=book.to_dict())

@app.route('/api/v1/authors/<int:author_id>', methods=['GET', 'POST','DELETE'])
def single_author(author_id):
    if type(author_id) == str:
        author = Author.query.filter_by(name=author_id).first_or_404()
    author = Author.query.filter_by(id=author_id).first_or_404()
    if request.method == 'DELETE':
        db.session.delete(author)
        db.session.commit()
        return{
            'success': 'Data deleted'
        }
    return jsonify(author.to_dict())
    # return render_template("author_detail.html", author=author.to_dict())

@app.route('/api/v1/authors/<int:author_id>/books', methods=['GET', 'POST','DELETE'])
def author_books(author_id):
    author = Author.query.filter_by(id=author_id).first_or_404()
    if request.method == 'DELETE':
        db.session.delete(author)
        db.session.commit()
        return{
            'success': 'Data deleted'
        }
    
    return jsonify([book.to_dict() for book in author.books])