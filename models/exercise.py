from init import db, ma

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_groups.id'), nullable=False)
    exercise_equipment_id = db.Column(db.Integer, db.ForeignKey('exercise_equipments.id'), nullable=False)
    logged_workouts = db.relationship('Logged_workout', backref='exercises')