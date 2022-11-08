# Importing to make a blueprint for routes and request.json returns json format from client aka postman.
from flask import Blueprint, request

# Importing marshmallow
from init import db

# Importing model User to be used in controller.
from models.user import User, UserSchema

# Importing sql error to catch any integrity error.
from sqlalchemy.exc import IntegrityError

# Importing Flas_Bcrypt for Authentication purposes.
# It's use is to password hash a password given
from flask_bcrypt import Bcrypt

# Creating an instance of bycrypt for Authentication of our flask app.
bcrypt = Bcrypt()

# Blue print of users with a url prefix of /users/
users_bp = Blueprint('users', __name__, url_prefix='/users')

# route users lists all the users json, attached route to users_bp blueprint.
@users_bp.route('/')
# Checking if user has a bearer JWT token and hasn't expired.
# @jwt_required()
def get_all_users():
    # if not authorize():
    #     return {'error': 'You must be an admin'}, 401

    # Creating a SQL statement that looks up all users from the users table.
    stmt = db.select(User)
    # Inputting the statement into an sqlalchemy to select all user objects and inputting it into users variable.
    users = db.session.scalars(stmt)
    # Returning via many users and marshmallow, serializing through dump for Flask to jsonify users and return.
    # Data in JSON format. 
    return UserSchema(many=True).dump(users)


# Retrieving a specific user from the id number inputted in our end point.
@users_bp.route('/<int:id>/')
def get_one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    # Checking if user exists with the given id in the route given.
    if user:
        return UserSchema().dump(user)
    else:
        return {'error': f'User not found with the given id {id}'}, 404


# Creating a route to delete a user from the database.
@users_bp.route('/<int:id>/', methods=['DELETE'])
def delete_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    # Checking if user exists with the given id in the route given.
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f'User {user.username} deleted successfully'}
    else:
        return {'error': f'User not found with the given id {id}'}, 404


# Updating the inputted user information with PUT or PATCH methods.
@users_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
def update_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    # Checking if user exists with the given id in the route given.
    if user:
        user.username = request.json.get('username') or user.username
        user.email = request.json.get('email') or user.email
        user.password = user.password or bcrypt.generate_password_hash(request.json.get('password')).decode('utf8')
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'User not found with the given id {id}'}, 404        


# POST request of username and password in a json string 
@users_bp.route('/register/', methods=['POST'])
def create_user():
    # Create a new User model instance
    try:
        # We are sending the request through json format else it won't be sent any other way.
        # We can increase security by ensuring we use POST method and json body only. This prevents any SQL injection
        user = User(
            username = request.json['username'],
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
        )    

        # Add and commit user to DB
        db.session.add(user)
        db.session.commit()
        # Respond to client excluding the password from the client
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {"error" : "Email Address already in use"}, 409 
