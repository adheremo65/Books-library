#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
from models import User,Review,Book, Rating

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        # Delete existing data
        User.query.delete()
        Book.query.delete()

        # Create and add users
        users = []
        for _ in range(20):
            password = fake.last_name()  # Set a plain text password
          
            user = User(
                name=fake.first_name(),
                email=fake.email(),
                password_hash=password
            )
            user.set_password(password) 
            # Set the hashed password
            users.append(user)

        db.session.add_all(users)
        db.session.commit()

        # Create and add books
        bookies = []
        for _ in range(20):
            book = Book(
                title=fake.catch_phrase(),
                author=fake.last_name()
            )
            bookies.append(book)

        db.session.add_all(bookies)
        db.session.commit()