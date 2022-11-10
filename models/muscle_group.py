# Importing local module init that contains our instances of dependencies for Flask. 
from init import db, ma

# Created the muscle group model with its corresponding columns.
class Muscle_group(db.Model):
    __tablename__ = 'muscle_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationship with muscle group and exercises.
    exercises = db.relationship('Exercise', back_populates='muscle_group')

# Created the coressponding schema for muscle group model.
class Muscle_groupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')