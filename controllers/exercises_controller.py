# Importing to make a blueprint for routes and request.json returns json format from client aka postman.
from flask import Blueprint, request

# Importing marshmallow
from init import db

# Importing model User to be used in controller.
from models.exercise import Exercise, ExerciseSchema

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
exercises_bp = Blueprint('exercises', __name__, url_prefix='/exercises')

# route users lists all the exercises json, attached route to exercises_bp blueprint.
@exercises_bp.route('/')
# Checking if user has a bearer JWT token and hasn't expired.
@jwt_required()
def get_all_exercises():
    # Creating a SQL statement that looks up all exercises from the listed exercise table.
    stmt = db.select(Exercise)
    # Inputting the statement into an sqlalchemy to select all exercise objects and inputting it into exercises variable.
    exercises = db.session.scalars(stmt)
    # Returning via exercises and marshmallow, serializing through dump for Flask to jsonify exercises and return.
    # Data in JSON format. 
    return ExerciseSchema(many=True).dump(exercises)

# Creating a route to delete an exercise from the database.
@exercises_bp.route('/<int:id>/', methods=['DELETE'])
# Checking for sign in token.
@jwt_required()
def delete_exercise(id):
    # Authorization added so only admins can delete exercises.
    authorize()
    # Creating statement to check Exercise model for the id put into endpoint.
    stmt = db.select(Exercise).filter_by(id=id)

    # Placing statement into database to look for a single object and storing it in exercise.
    exercise = db.session.scalar(stmt)
    # Checking if exercise exists with the given id in the route given.
    if exercise:
        db.session.delete(exercise)
        db.session.commit()
        return {'message': f'Exercise {exercise.name} deleted successfully'}
    else:
        return {'error': f'Exercise not found with the given id {id}'}, 404

