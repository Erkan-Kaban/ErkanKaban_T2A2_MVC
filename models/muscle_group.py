from init import db, ma

class Muscle_group(db.Model):
    __tablename__ = 'muscle_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exercises = db.relationship('Exercise', back_populates='muscle_group')

class Muscle_groupSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')