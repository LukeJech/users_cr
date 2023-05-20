
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class User:
    db = "users_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models
    @classmethod
    def save_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES ( %(first_name)s, %(last_name)s, %(email)s)
        ;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        return result



    # Read Users Models
    @classmethod
    def get_all_users(cls):
        query = """
        SELECT * FROM users;
        """
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        
        for user in results: 
            users.append(cls(user))
        return users
    



    # Update Users Models



    # Delete Users Models