from init import db, ma

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    # cascade if you delete this user then with cascade all of their logged_workouts also get deleted.
    Logged_workout = db.relationship('Logged_workout', backref='user', cascade='all, delete')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password', 'is_admin')
        # In addition to the flask config order, we also need to specify the following
        ordered = True
        # ordered true aligns with what we specified in fields to show up in that order.

        