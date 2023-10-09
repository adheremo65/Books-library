from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, String, Integer, ForeignKey,MetaData
from sqlalchemy.orm import relationship
from config import db
from flask_sqlalchemy import SQLAlchemy


from flask_bcrypt import Bcrypt,check_password_hash

bcrypt = Bcrypt()


# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
# db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False, unique = True) 
    email = db.Column(db.String(255), unique=True, nullable=False)
    # password_hash = db.Column(db.String(60), nullable=False, default="")
    ratings = db.relationship("Rating", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")

    def __repr__(self):
        return f"<User: {self.name}>"

    # def set_password(self, password):
    #     self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    # def check_password(self, password):
    #     return bcrypt.check_password_hash(self.password_hash, password)

class Rating(db.Model,SerializerMixin):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    user = db.relationship("User", back_populates="ratings")
    book = db.relationship("Book", back_populates="ratings")

    def __repr__(self):
        return f"<Rating: {self.rating} for Book: {self.book.title}>"

class Review(db.Model,SerializerMixin):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    user = db.relationship("User", back_populates="reviews")
    book = db.relationship("Book", back_populates="reviews")

class Book(db.Model,SerializerMixin):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)

    reviews = db.relationship("Review", back_populates="book")
    ratings = db.relationship("Rating", back_populates="book")

    def __repr__(self):
        return f"<Book: {self.title}, Author: {self.author}>"

