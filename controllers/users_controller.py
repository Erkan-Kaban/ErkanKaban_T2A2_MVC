# Importing to make a blueprint for routes.
from flask import Blueprint

# Importing marshmallow
from init import db

from models.user import User, UserSchema

# Blue print of users with a url prefix of /users/
users_bp = Blueprint('users', __name__, url_prefix='/users')

# route users lists all the users json, attached route to users_bp blueprint.
@users_bp.route('/')
# Checking if user has a bearer JWT token and hasn't expired.
# @jwt_required()
def all_users():
    # if not authorize():
    #     return {'error': 'You must be an admin'}, 401

    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True).dump(users)

@users_bp.route('/<int:id>/')
def single_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    return UserSchema().dump(user)
