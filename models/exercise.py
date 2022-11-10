# Importing local module init that contains our instances of dependencies for Flask. 
from init import db, ma
from marshmallow import fields

# Created the exercise model with its corresponding columns.
class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    # ForeignKey's from muscle_groups and exercise equipments
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_groups.id'), nullable=False)
    exercise_equipment_id = db.Column(db.Integer, db.ForeignKey('exercise_equipments.id'), nullable=False)

    # Relationship with muscle group, exercise equipment.
    muscle_group = db.relationship('Muscle_group', back_populates='exercises')
    exercise_equipment = db.relationship('Exercise_equipment', back_populates='exercises')

    # Relationship with logged_workouts and exercises.
    logged_workouts = db.relationship('Logged_workout', back_populates='exercise')

# Created the coresponding schema for the Exercise model.
class ExerciseSchema(ma.Schema):
    # Created a nested schema to view the name of the muscle group for that particular exercise.
    muscle_group = fields.Nested('Muscle_groupSchema', only=['name'])

    # Created a nested schema to view the name of the exercise equipment used for that particular exercise.
    exercise_equipment = fields.Nested('Exercise_equipmentSchema', only=['name'])

    class Meta:
        fields = ('id', 'name', 'muscle_group_id', 'muscle_group', 'exercise_equipment_id', 'exercise_equipment')
        # In addition to the flask config order, we also need to specify the following
        ordered = True
        # ordered true aligns with what we specified in fields to show up in that order.