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

# Retrieving a specific exercise from the id number inputted in our end point.
@exercises_bp.route('/<int:id>/')
@jwt_required()
def get_one_exercise(id):
    stmt = db.select(Exercise).filter_by(id=id)
    exercise = db.session.scalar(stmt)
    # Checking if exercise exists with the given id in the route given.
    if exercise:
        return ExerciseSchema().dump(exercise)
    else:
        return {'error': f'Exercise not found with the given id {id}'}, 404


# POST creation of a workout, only admins allowed. 
@exercises_bp.route('/add-workout/', methods=['POST'])
@jwt_required()
def create_exercise():
    # Create a new User model instance
    data = ExerciseSchema().load(request.json)
    # Authorization added so only admins can create workouts to library.
    authorize()
    # Create a new Exercise model instance
    try:
        # We are sending the request through json format else it won't be sent any other way.
        # We can increase security by ensuring we use POST method and json body only. This prevents any SQL injection
        exercise = Exercise(
            name = data['name'],
            muscle_group_id = data['muscle_group_id'],
            exercise_equipment_id = data['exercise_equipment_id']
        )    
        # Add and commit exercise to DB
        db.session.add(exercise)
        db.session.commit()
        # Respond to client excluding the password from the client
        return ExerciseSchema().dump(exercise), 201
    except IntegrityError:
        return {"error" : "exercise already created or requires a valid exercise id."}, 409


# Updating the inputted exercise with PUT or PATCH methods.
@exercises_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_exercise(id):
    # Create a new User model instance
    data = ExerciseSchema().load(request.json)
    # Authorization checks if exercise is admin.
    authorize()
    stmt = db.select(Exercise).filter_by(id=id)
    exercise = db.session.scalar(stmt)
    # Checking if exercise exists with the given id in the route given.
    if exercise:
        exercise.name = data['name'] or exercise.name
        exercise.muscle_group_id = data['muscle_group_id'] or exercise.muscle_group_id
        exercise.exercise_equipment_id = data['exercise_equipment_id'] or exercise.exercise_equipment_id
        db.session.commit()
        return ExerciseSchema().dump(exercise)
    else:
        return {'error': f'Exercise not found with the given id {id}'}, 404  

@exercises_bp.route('/muscle-group/<int:muscle>/')
@jwt_required()
def get_muscle_group(muscle):
    stmt = db.select(Exercise).filter_by(muscle_group_id = muscle)
    muscle_group = db.session.scalars(stmt)
    return ExerciseSchema(many=True).dump(muscle_group)


