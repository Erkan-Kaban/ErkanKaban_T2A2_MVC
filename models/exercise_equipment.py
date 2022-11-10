# Importing local module init that contains our instances of dependencies for Flask. 
from init import db, ma

# Created the exercise equipment model with its corresponding columns.
class Exercise_equipment(db.Model):
    __tablename__ = 'exercise_equipments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationship with Exercise table.
    exercises = db.relationship('Exercise', backref='exercise_equipments')

    # Created the coressponding schema for muscle group model.
class Exercise_equipmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')