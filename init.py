# Importing Marshmallow for Flask
from flask_marshmallow import Marshmallow

# Importing ORM SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy

# Creating an instance of marshmallow and passing our flask app
ma = Marshmallow()

# Creating a new instance of SQLAlchemy that passes in our app variable returning a db object to access the database.
db = SQLAlchemy()