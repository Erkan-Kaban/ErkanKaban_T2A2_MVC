# Importing marshmallow and sqlalchemy.
from init import db, ma

# importing fields from marshmallow.
from marshmallow import fields

# Importing Validation modules from marshmallow.
from marshmallow.validate import Length, Regexp, And, Email

# Created the User model.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # cascade if you delete this user then with cascade all of their logged_workouts also get deleted.
    logged_workouts = db.relationship('Logged_workout', back_populates='users', cascade='all, delete')

class UserSchema(ma.Schema):
    # Validations.
    # Checking if username is a minimum of 3 characters.
    # Checking regexp are regular expressions we are allowed to use for username.
    username = fields.String(required=True, validate=And(
        Length(min=3, error='Username must be at least 5 characters long'),
        Regexp('^[A-zA-Z0-9 ]+$', error='Only letters, numbers and spaces are allowed')
    ))

    # Created an email validator, making sure we require an @
    email = fields.String(required=False, validate=And(
        Email(error='Email requires correct format')
    ))
   
    class Meta:
        # fields set for dump
        fields = ('id', 'username', 'email', 'password', 'is_admin')
        # In addition to the flask config order, we also need to specify the following
        ordered = True
        # ordered true aligns with what we specified in fields to show up in that order.

        