# from models import Review,Book,User,Category,BookCategory

# Remote library imports
import ipdb 



#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
from models import Review,Book,User,Category,BookCategory,Rating

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        from models import Review,Book,User,Category,BookCategory

        from models import db
        
        # book = Book.query.first()
        # bc = book.categories
        # for cat in bc:
        #     print(cat.category.cate_name)

        ipdb.set_trace()
