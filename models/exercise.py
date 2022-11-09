from init import db, ma
from marshmallow import fields

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_groups.id'), nullable=False)
    exercise_equipment_id = db.Column(db.Integer, db.ForeignKey('exercise_equipments.id'), nullable=False)

    muscle_group = db.relationship('Muscle_group', back_populates='exercises')
    # logged_workouts = db.relationship('Logged_workout', back_populates='exercises')

class ExerciseSchema(ma.Schema):
    muscle_group = fields.Nested('Muscle_groupSchema', only=['name'])

    class Meta:
        fields = ('id', 'name', 'muscle_group_id', 'exercise_equipment_id', 'muscle_group')
        # In addition to the flask config order, we also need to specify the following
        ordered = True
        # ordered true aligns with what we specified in fields to show up in that order.