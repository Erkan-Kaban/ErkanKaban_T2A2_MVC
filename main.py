# Importing Flask, jsonify and request.json returns json format from client (postman)
from flask import Flask

# Importing sqlalchemy and marshmallow.
from init import db, ma, bcrypt, jwt

# For use for app.config to use our .env file to configuration.
import os

# Importing validation error from marshmallow
from marshmallow.exceptions import ValidationError

# Importing blueprint from controllers
from controllers.users_controller import users_bp
from controllers.auth_controller import auth_bp
from controllers.cli_controller import db_commands
from controllers.exercises_controller import exercises_bp
from controllers.logged_workout_controller import logged_workout_bp
from controllers.user_stat_controller import user_stats_bp
from sqlalchemy.exc import DataError 

# Flask will automatically look for create_app and run it.
def create_app():
    # Creating an instance of Flask and calling the variable name 'app'.
    app = Flask(__name__)
    
    # Catches any validation errors.
    @app.errorhandler(ValidationError)
    def validation_error(err):
        # catch the error 400 a return the html error in JSON format.
        return {'error': err.messages}, 400

    @app.errorhandler(TypeError)
    def type_error(err):
        return {'error': err}, 400

    @app.errorhandler(DataError)
    def data_error(err):
        # catch the error 400 a return the html error in JSON format.
        return {'error': err}, 400

    # Catches any empty inputs
    @app.errorhandler(400)
    def bad_request(err):
        # catch the error 400 a return the html error in JSON format.
        return {'error': str(err)}, 400

    # A global error catcher for our entire app. Used here for DRY code, rather than adding in individual controllers. 
    @app.errorhandler(404)
    def not_found(err):
        # catch the error 404 a return the html error in JSON format.
        return {'error': str(err)}, 404

    # Handles any unauthorized errors.
    @app.errorhandler(401)
    def unauthorized(err):
        # catch the error 401 a return the html error in JSON format.
        return {'error': str(err)}, 401

    # Handles any key errors.
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    # flask automatically sorts our columns in alphabetical order
    # To get the order we want specified in our schemas we need to do the following to the config
    app.config['JSON_SORT_KEYS'] = False

    # Creating a config for flask to setup sql alchemy with our adapter psycopg2 to communicate with our psql db.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # Setting up the secret key that the jwt manager will use to encrypt the token
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    # We are able split the creation and declaration of the app object inside create app function and globally.
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Attaches blueprints to Flask application.
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(db_commands)
    app.register_blueprint(exercises_bp)
    app.register_blueprint(logged_workout_bp)
    app.register_blueprint(user_stats_bp)

    return app