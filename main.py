# Importing Flask, jsonify and request.json returns json format from client aka postman.
from flask import Flask, jsonify, request

# Importing ORM SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy

import os

# Flask will automatically look for create_app and run it.
def create_app():
    app = Flask(__name__)
    # Creating a config for flask to setup sql alchemy with our adapter psycopg2 to communicate with our psql db.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # Creating a new instance of SQLAlchemy that passes in our app variable returning a db object to access the database.
    db = SQLAlchemy(app)

    return app