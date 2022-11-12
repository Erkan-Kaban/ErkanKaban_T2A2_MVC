# Importing to make a blueprint for routes and request.json returns json format from client aka postman.
from flask import Blueprint, request

# Importing marshmallow
from init import db

# Importing model User to be used in controller.
from models.user_stat import User_stat, User_statSchema

# Importing sql error to catch any integrity error.
from sqlalchemy.exc import IntegrityError

# Importing Flas_Bcrypt for Authentication purposes.
# It's use is to password hash a password given
from flask_bcrypt import Bcrypt

# Checking for tokens authentication
from flask_jwt_extended import jwt_required

# Importing out authentication module from auth controller
from controllers.auth_controller import authorize, authorize_user

# Creating an instance of bycrypt for Authentication of our flask app.
bcrypt = Bcrypt()

# Blue print of users statistics with a url prefix of /user-stats
user_stats_bp = Blueprint('user_stats', __name__, url_prefix='/user-stats')

# route users lists all the exercises json, attached route to exercises_bp blueprint.
@user_stats_bp.route('/')
# Checking if user has a bearer JWT token and hasn't expired.
@jwt_required()
def get_all_user_stats():
    # Only admins can look at all user stats.
    authorize()
    # Creating a SQL statement that looks up all user_stats.
    stmt = db.select(User_stat)
    # Inputting the statement into an sqlalchemy to select all user_stats objects and inputting it into user_stats variable.
    user_stats = db.session.scalars(stmt)
    # Returning via user_stat and marshmallow, serializing through dump for Flask to jsonify user_stat and return.
    # Data in JSON format. 
    return User_statSchema(many=True).dump(user_stats)

# Creating a route to delete a users stats from the database.
@user_stats_bp.route('/<int:user_id>/', methods=['DELETE'])
# Checking for sign in token.
@jwt_required()
def delete_user_stat(user_id):
    # Authorization added so only user can delete.
    authorize_user(user_id)
    # Creating statement to check user_stat model for the id put into endpoint.
    stmt = db.select(User_stat).filter_by(user_id=user_id)
    # Placing statement into database to look for a single object and storing it in user_stat.
    user_stat = db.session.scalar(stmt)
    # Checking if user_stat exists with the given id in the route given.
    if user_stat:
        db.session.delete(user_stat)
        db.session.commit()
        return {'message': f'User Stat id {user_stat.user_id} deleted successfully'}
    else:
        return {'error': f'User stat not found with the given id {user_id}'}, 404

# Retrieving a specific user stat from the id number inputted in our end point.
@user_stats_bp.route('user/<int:user_id>/')
@jwt_required()
def get_one_userstat(user_id):
    # Authorization added so only user can delete.
    authorize_user(user_id)
    stmt = db.select(User_stat).filter_by(user_id=user_id)
    user_stat = db.session.scalar(stmt)
    # Checking if user_id exists with the given id in the route given.
    if user_stat:
        return User_statSchema().dump(user_stat)
    else:
        return {'error': f'user stat not found with the given id {user_stat}'}, 404

# POST creation of a user-stat, only user allowed. 
@user_stats_bp.route('user/add-stats/<int:user_id>/', methods=['POST'])
@jwt_required()
def create_user_stat(user_id):
    # Authorization added so only user can delete.
    authorize_user(user_id)

    # We are checking if the user already exists, as each user id is supposed to only have one set
    # of statistics.
    stmt = db.select(User_stat).filter_by(user_id=user_id)
    user_stat = db.session.scalar(stmt)
    if user_stat:
        return {'error': 'user stat already exists'}
        
    # Create a new user_stat model instance
    data = User_statSchema().load(request.json)
    try:
        # We are sending the request through json format else it won't be sent any other way.
        # We can increase security by ensuring we use POST method and json body only. This prevents any SQL injection
        user_stat = User_stat(
        body_weight = data['body_weight'],
        height = data['height'],
        user_id = user_id
        )    
        # Add and commit user_stat to DB
        db.session.add(user_stat)
        db.session.commit()
        # Respond to client excluding the password from the client
        return User_statSchema().dump(user_stat), 201
    except IntegrityError:
        return {"error" : "user_stat already created"}, 409
    except TypeError:
        return {"error" : "user_stat already created"}, 409


# Updating the inputted exercise with PUT or PATCH methods.
@user_stats_bp.route('user/<int:user_id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user_stat(user_id):
    # Authorization added so only user can delete.
    authorize_user(user_id)
    stmt = db.select(User_stat).filter_by(user_id=user_id)
    user_stat = db.session.scalar(stmt)
    # Checking if exercise exists with the given id in the route given.
    if user_stat:
        user_stat.body_weight = request.json.get('body_weight') or user_stat.body_weight
        user_stat.height = request.json.get('height') or user_stat.height
        db.session.commit()
        return User_statSchema().dump(user_stat)
    else:
        return {'error': f'User stat not found with the given id {user_id}'}, 404 


