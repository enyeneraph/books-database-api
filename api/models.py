from sqlalchemy import Column, ForeignKey
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    genre = db.Column(db.String)
    height = db.Column(db.Integer)
    publisher = db.Column(db.String)

    def __repr__(self):
        return f'<Book {self.title}>'

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author.to_dict(),
            "genre": self.genre,
            "height": self.height,
            "publisher": self.publisher
            }

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    books = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f'<Author {self.id}>'

    def to_dict(self):
        book_list = []
        for book in self.books:
            book_list.append(book.id)
        return {
            "id":self.id,
            "name": self.name,
            "location": self.location,
            "age": self.age,
            "gender": self.gender,
            "num_of_books": len(self.books),
            "books": book_list
        }

    # def to_dict(self):
    #     book_list = []
    #     for book in self.books:
    #         book_list.append(book.to_dict())
    #     init_dict = self.for_books_to_dict()
    #     init_dict['books'] = book_list
    #     return init_dict
        
