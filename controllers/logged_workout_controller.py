# Importing to make a blueprint for routes and request.json returns json format from client aka postman.
from flask import Blueprint, request

# Importing marshmallow
from init import db

# Importing model User to be used in controller.
from models.logged_workout import Logged_workout, Logged_workoutSchema

# Importing sql error to catch any integrity error.
from sqlalchemy.exc import IntegrityError

# Importing Flas_Bcrypt for Authentication purposes.
# It's use is to password hash a password given
from flask_bcrypt import Bcrypt

# Checking for tokens authentication
from flask_jwt_extended import jwt_required

# Importing out authentication module from auth controller
from controllers.auth_controller import authorize

# Creating an instance of bycrypt for Authentication of our flask app.
bcrypt = Bcrypt()

# Blue print of workouts with a url prefix of /workouts
logged_workout_bp = Blueprint('logged_workouts', __name__, url_prefix='/workouts')

# route logged_workout_bp lists all the workouts.
@logged_workout_bp.route('/')
# Checking if user has a bearer JWT token and hasn't expired.
@jwt_required()
def get_all_workouts():
    # Authorization added so only admins view everyones exercises.
    authorize()
    # Creating a SQL statement that looks up all workouts from the listed logged work out table.
    stmt = db.select(Logged_workout)
    print(stmt)
    # Inputting the statement into an sqlalchemy to select all workout objects and inputting it into stmt variable.
    workouts = db.session.scalars(stmt)
    # Returning via workouts and marshmallow, serializing through dump for Flask to jsonify workouts and return.
    # Data in JSON format. 
    return Logged_workoutSchema(many=True).dump(workouts)

# route logged_workout_bp lists all the workouts.
@logged_workout_bp.route('/<int:user_id>')
def get_user_workout(user_id):
    # Creating a statement that checks for matching user id
    stmt = db.select(Logged_workout).filter_by(id=user_id)
    # Placing statement into database to look for the object.
    logged_workout = db.session.scalar(stmt)
    print(logged_workout)
    return Logged_workoutSchema().dump(logged_workout)