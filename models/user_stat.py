# Importing local module init that contains our instances of dependencies for Flask.
from init import db, ma
from sqlalchemy.orm import backref
from marshmallow import fields
# Importing Validation modules from marshmallow.
from marshmallow.validate import Range

# Created the exercise model with its corresponding columns.
class User_stat(db.Model):
    __tablename__ = 'user_stats'
    id = db.Column(db.Integer, primary_key=True)
    body_weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    # Foreign key.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)

    # relationship one to one with user.
    user = db.relationship('User', backref=backref('user_stat', uselist=False))

class User_statSchema(ma.Schema):
    # Validations.
    # Checks if the user enters a valid integer between a range.
    body_weight = fields.Integer(validate=Range(min=2, max=400))
    height = fields.Integer(validate=Range(min=120, max=250))

    # Creating a nesting schema to show users name.
    user = fields.Nested('UserSchema', only=['username'])

    class Meta:
        fields = ('id', 'body_weight', 'height', 'user_id', 'user')
    

