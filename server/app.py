#!/usr/bin/env python3
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
# Standard library imports
from flask import Flask,request,jsonify,session
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from config import app, db, api,cors
from models import User,Book,Rating,Review
from flask_session import Session
import os
import secrets




# Local imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports

# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'
@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        password = request.form.get("password")
        email = request.form.get("email")

        user = User.query.filter_by(email=email).first() is not None
        if  user:
            return jsonify({"error":"User already exists"},409)
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(email=email,password = hashed_password,name = name)
        db.session.add(new_user)
        db.session.commit()
        
        session["user_id"]= new_user.id
        return jsonify({
            "id":new_user.id,
            "email":new_user.email

        })
        

@app.route("/login", methods=["POST"])
def login():
        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")  
            user = User.query.filter_by(email=email).first()
        if user is None:
            return jsonify({"error": "Unauthorized"}), 401
    #checking if the password is the same as hashed password
        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error": "Unauthorized"}), 401
        
        session["user_id"] = user.id
        return jsonify({
            "id": user.id,
            "email": user.email
        })
        
        
@app.route("/logout", methods=["POST"])
def logout():
    if "user_id" in session:
        session.pop("user_id")
        return "Logged out successfully", 200
    else:
        return "User is not logged in", 401

@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
        "email": user.email
    },200) 
        
if __name__ == '__main__':
    app.run(port=5555, debug=True, host='localhost')

