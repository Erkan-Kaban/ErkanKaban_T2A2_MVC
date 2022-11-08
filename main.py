# Importing Flask, jsonify and request.json returns json format from client (postman)
from flask import Flask, jsonify, request

# Importing sqlalchemy and marshmallow.
from init import db, ma

# For use for app.config to use our .env file to configuration.
import os

# Importing blueprint from controllers/users_controller.
from controllers.users_controller import users_bp

# Flask will automatically look for create_app and run it.
def create_app():
    app = Flask(__name__)

    # flask automatically sorts our columns in alphabetical order
    # To get the order we want specified in our schemas we need to do the following to the config
    app.config['JSON_SORT_KEYS'] = False

    # Creating a config for flask to setup sql alchemy with our adapter psycopg2 to communicate with our psql db.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # We are able split the creation and declaration of the app object inside create app function and globally.
    db.init_app(app)
    ma.init_app(app)

    # Attaches blueprints to Flask application.
    app.register_blueprint(users_bp)

    return app