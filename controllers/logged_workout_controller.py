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

# Blue print of exercises with a url prefix of /exercises
logged_workout_bp = Blueprint('logged_workouts', __name__, url_prefix='/workouts')

# route logged_workout_bp lists all the worksouts.
@logged_workout_bp.route('/')
# Checking if user has a bearer JWT token and hasn't expired.
@jwt_required()
def get_all_workouts():
    # Creating a SQL statement that looks up all workouts from the listed exercise table.
    stmt = db.select(Logged_workout)
    print(stmt)
    # Inputting the statement into an sqlalchemy to select all workout objects and inputting it into stmt variable.
    workouts = db.session.scalars(stmt)
    # Returning via exercises and marshmallow, serializing through dump for Flask to jsonify exercises and return.
    # Data in JSON format. 
    return Logged_workoutSchema(many=True).dump(workouts)