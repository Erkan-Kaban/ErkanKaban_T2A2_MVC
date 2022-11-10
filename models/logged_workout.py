# Importing local module init that contains our instances of dependencies for Flask. 
from init import db, ma
from marshmallow import fields

# Created the logged workout model with its corresponding columns.
class Logged_workout(db.Model):
    __tablename__ = 'logged_workouts'

    id = db.Column(db.Integer, primary_key=True)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    # ForeignKey's from exercises and users table.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)

    # Relationship with logged workout and users.
    # exercise = db.relationship('Exercise', back_populates='logged_workout')

# Created the coresponding schema for the logged_workout model.
class Logged_workoutSchema(ma.Schema):
    # created a nested schema that contains the name of the exercise in a logged workout.
    exercise = fields.Nested('ExerciseSchema', only=['name'])

    class meta:
        fields = ('id', 'sets', 'reps', 'weight', 'exercise')