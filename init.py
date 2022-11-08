# Importing Marshmallow for Flask
from flask_marshmallow import Marshmallow

# Importing ORM SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy

# Importing Flas_Bcrypt for Authentication purposes.
# It's use is to password hash a password given
from flask_bcrypt import Bcrypt

# Importing JWT to create jason web tokens.
# jwt required is to a used decorator to check for a token for a certain end point.
# jwt identity checks if user is authorized or admin
from flask_jwt_extended import JWTManager

# Creating an instance of marshmallow and passing our flask app
ma = Marshmallow()

# Creating a new instance of SQLAlchemy that passes in our app variable returning a db object to access the database.
db = SQLAlchemy()

# Creating an instance of bycrypt for Authentication of our flask app.
bcrypt = Bcrypt()

# Initializing JWT manager to the Flask Application
jwt = JWTManager()