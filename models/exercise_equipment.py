from init import db, ma

class Exercise_equipment(db.Model):
    __tablename__ = 'exercise_equipments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    exercises = db.relationship('Exercise', backref='exercise_equipments')