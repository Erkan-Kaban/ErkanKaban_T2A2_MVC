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
from controllers.auth_controller import authorize, authorize_user

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
# with route user_id inputted the user with the matching id can only access this route
@logged_workout_bp.route('user/<int:user_id>')
@jwt_required()
def get_user_workout(user_id):
    # Authorize user checking if it's the matching user
    authorize_user(user_id)
    # Creating a statement that checks for matching user id
    stmt = db.select(Logged_workout).filter_by(user_id=user_id)
    # Placing statement into database to look for the object.
    logged_workout = db.session.scalars(stmt)
    return Logged_workoutSchema(many=True).dump(logged_workout)

# Updating the user id's exercise with PUT or PATCH methods.
@logged_workout_bp.route('user/<int:user_id>/exercise/<int:exercise_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user_workout(user_id, exercise_id):
    # Authorize user checking if it's the matching user
    authorize_user(user_id)
    stmt = db.select(Logged_workout).filter_by(id=exercise_id)
    user = db.session.scalar(stmt)
    # Checking if user exists with the given id in the route given.
    if user:
        user.sets = request.json.get('sets') or user.sets
        user.reps = request.json.get('reps') or user.reps
        user.weight = request.json.get('weight') or user.weight
        db.session.commit()
        return Logged_workoutSchema().dump(user)
    else:
        return {'error': f'Exercise not found with the given id {exercise_id}'}, 404

# POST creation of a workout for a specific user.
@logged_workout_bp.route('/add/user/<int:user_id>/', methods=['POST'])
@jwt_required()
def create_exercise(user_id):
    # Authorize user checking if it's the matching user
    authorize_user(user_id)
    # Create a new logged_workout model instance
    try:
        # We are sending the request through json format else it won't be sent any other way.
        # We can increase security by ensuring we use POST method and json body only. This prevents any SQL injection
        logged_workout = Logged_workout(
            sets = request.json['sets'],
            reps = request.json['reps'],
            weight = request.json['weight'],
            user_id = user_id,
            exercise_id = request.json['exercise_id']
        )  
        # Add and commit exercise to DB
        db.session.add(logged_workout)
        db.session.commit()
        # Respond to client excluding the password from the client
        return Logged_workoutSchema().dump(logged_workout), 201
    except IntegrityError:
        return {"error" : "exercise already created"}, 409
    except TypeError:
        return {"error": "Please enter an integer"}, 400 

# Creating a route to delete a logged workout from the database.
@logged_workout_bp.route('/delete/user/<int:user_id>/exercise/<int:exercise_id>', methods=['DELETE'])
# Checking for sign in token.
@jwt_required()
def delete_exercise(user_id, exercise_id):
    # Authorize user checking if it's the matching user
    authorize_user(user_id)
    # Creating statement to check Exercise model for the id put into endpoint.
    stmt = db.select(Logged_workout).filter_by(id=exercise_id)
    # Placing statement into database to look for a single object and storing it in exercise.
    workout = db.session.scalar(stmt)
    # Checking if exercise exists with the given id in the route given.
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return {'message': f'Exercise id {workout.exercise_id} deleted successfully'}
    else:
        return {'error': f'Exercise not found with the given id {exercise_id}'}, 404