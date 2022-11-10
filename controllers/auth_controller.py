from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import date, timedelta
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

# Blue print of authentication with a url prefix of /users/
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login/', methods=['POST'])
def auth_login():
    # A SQL request that checks the User database for the email written by user.
    stmt = db.select(User).filter_by(email=request.json['email'])
    # We get the single user from the stmt (statement) variable 
    user = db.session.scalar(stmt)
    # If the inputted user is True then Authentication is successful with a json response excluding password information
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        # We create a token for that particular user with a time expiry of 1 day
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        # return the email as information, the token and whether their admin or not.
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email or password'}, 401


# POST request of username and password in a json string 
@auth_bp.route('/register/', methods=['POST'])
def auth_register():
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

# Creating a authorization function that can be imported from other modules. 
# Authorize checks if the user is admin is True, upon registration its default is False.
def authorize():
    # get the jwt token from the user
    user_id = get_jwt_identity()
    # SQL statement that filters the user_id with id's in the user model.
    stmt = db.select(User).filter_by(id=user_id)
    # We send this statement into a db.session and save it in user.
    user = db.session.scalar(stmt)
    # return user is admin is true or false
    if not user.is_admin:
        abort(401)

def authorize_user(id):
    # get the jwt token from the user
    user_id = get_jwt_identity()
    # SQL statement that filters the user_id with id's in the user model.
    stmt = db.select(User).filter_by(id=user_id)
    # We send this statement into a db.session and save it in user.
    user = db.session.scalar(stmt)
    # return user is admin is true or false
    if user.id != id:
        abort(401)
