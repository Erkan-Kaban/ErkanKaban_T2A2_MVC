from flask import Blueprint
from init import db, bcrypt
from models.logged_workout import Logged_workout
from models.user import User
from models.exercise import Exercise
from models.muscle_group import Muscle_group
from models.exercise_equipment import Exercise_equipment
from models.user_stat import User_stat



db_commands = Blueprint('db', __name__)

# Defining custom commands CLI(terminal) for Flask
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")
	
@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Table dropped")

@db_commands.cli.command('seed')
def seed_db():

   # Seeding Users
   users = [
        User(
            username = 'Adam',
            email = 'Adam96@gmail.com',
            # Decoding hexadecimal has password into utf-8 string format, this string cannot be decrypted
            password = bcrypt.generate_password_hash('123').decode('utf-8'),
        ),
        User(
            username = 'Admin1',
            email = 'AdminMaster90@gmail.com',
            # Decoding hexadecimal has password into utf-8 string format, this string cannot be decrypted
            password = bcrypt.generate_password_hash('123').decode('utf-8'),
            is_admin = True
        ),
        User(
            username = 'Admin2',
            email = 'AdminMaster91@gmail.com',
            # Decoding hexadecimal has password into utf-8 string format, this string cannot be decrypted
            password = bcrypt.generate_password_hash('123').decode('utf-8'),
            is_admin = True
        ),
         User(
            username = 'Berni',
            email = 'BerniWong@gmail.com',
            # Decoding hexadecimal has password into utf-8 string format, this string cannot be decrypted
            password = bcrypt.generate_password_hash('123').decode('utf-8'),
        ),
        User(
            username = 'Kam',
            email = 'Kam@gmail.com',
            # Decoding hexadecimal has password into utf-8 string format, this string cannot be decrypted
            password = bcrypt.generate_password_hash('123').decode('utf-8'),
        ),
        User(
            username = 'Steve',
            email = 'Steve@gmail.com',
            # Decoding hexadecimal has password into utf-8 string format, this string cannot be decrypted
            password = bcrypt.generate_password_hash('123').decode('utf-8'),
        )
   ]

   # Seeding logged_workouts
   logged_work = [
        Logged_workout(
            sets = 3,
            reps = 10,
            weight = 50,
            user_id = 1,
            exercise_id = 1
        ),
        Logged_workout(
            sets = 5,
            reps = 10,
            weight = 20,
            user_id = 1,
            exercise_id = 2
        ),
        Logged_workout(
            sets = 2,
            reps = 10,
            weight = 10,
            user_id = 2,
            exercise_id = 5
        ),
        Logged_workout(
            sets = 5,
            reps = 2,
            weight = 10,
            user_id = 4,
            exercise_id = 2
        ),
        Logged_workout(
            sets = 1,
            reps = 5,
            weight = 100,
            user_id = 2,
            exercise_id = 9
        ),
        Logged_workout(
            sets = 3,
            reps = 8,
            weight = 150,
            user_id = 1,
            exercise_id = 1
        ),
        Logged_workout(
            sets = 3,
            reps = 10,
            weight = 150,
            user_id = 1,
            exercise_id = 10
        ),
        Logged_workout(
            sets = 3,
            reps = 10,
            weight = 150,
            user_id = 2,
            exercise_id = 10
        )
        
        
   ]
   # Seeding exercises
   exercises = [
        Exercise(
            name = 'Push-up',
            muscle_group_id = 5,
            exercise_equipment_id = 11
        ),
        Exercise(
            name = 'Plank',
            muscle_group_id = 5,
            exercise_equipment_id = 11
        ),
        Exercise(
            name = 'Push-up',
            muscle_group_id = 5,
            exercise_equipment_id = 11
        ),
        Exercise(
            name = 'Flat Bench Press',
            muscle_group_id = 5,
            exercise_equipment_id = 2
        ),
        Exercise(
            name = 'Incline D.B Chest Press',
            muscle_group_id = 5,
            exercise_equipment_id = 2
        ),
        Exercise(
            name = 'Cable Chest Flys',
            muscle_group_id = 5,
            exercise_equipment_id = 8
        ),
        Exercise(
            name = 'DB Lateral Raises',
            muscle_group_id = 4,
            exercise_equipment_id = 1
        ),
        Exercise(
            name = 'DB Skull Crusher',
            muscle_group_id = 3,
            exercise_equipment_id = 1
        ),
        Exercise(
            name = 'Tricep Rope Pushdown',
            muscle_group_id = 3,
            exercise_equipment_id = 8
        ),
        Exercise(
            name = 'BB Row',
            muscle_group_id = 2,
            exercise_equipment_id = 3
        ),
        Exercise(
            name = 'Lat Pulldown',
            muscle_group_id = 2,
            exercise_equipment_id = 6
        ),
        Exercise(
            name = 'T-Bar Row',
            muscle_group_id = 2,
            exercise_equipment_id = 3
        ),
        Exercise(
            name = 'Incline Bicep Curls',
            muscle_group_id = 1,
            exercise_equipment_id = 2
        ),
        Exercise(
            name = 'Hammer Curls',
            muscle_group_id = 1,
            exercise_equipment_id = 1
        ),
        Exercise(
            name = 'BB Back Squat',
            muscle_group_id = 6,
            exercise_equipment_id = 3
        ),
        Exercise(
            name = 'Leg Press',
            muscle_group_id = 6,
            exercise_equipment_id = 7
        ),
        Exercise(
            name = 'Lying Leg Curls',
            muscle_group_id = 6,
            exercise_equipment_id = 4
        ),
        Exercise(
            name = 'Rear Delt Flys',
            muscle_group_id = 4,
            exercise_equipment_id = 8
        ),
        Exercise(
            name = 'Calf Raises',
            muscle_group_id = 7,
            exercise_equipment_id = 10
        )
   ]

   # Seeding exercise_equipments
   exercise_equipments = [
        Exercise_equipment(
            name = 'Dumbbells'
        ),
        Exercise_equipment(
            name = 'Bench'
        ),
        Exercise_equipment(
            name = 'Olympic Bar plus plates combo'
        ),
        Exercise_equipment(
            name = 'Leg curl Machine'
        ),
        Exercise_equipment(
            name = 'Smith Machine'
        ),
        Exercise_equipment(
            name = 'Row Machine'
        ),
        Exercise_equipment(
            name = 'Leg Press Machine'
        ),
        Exercise_equipment(
            name = 'Cable Crossover Machine'
        ),
        Exercise_equipment(
            name = 'Glute Machine'
        ),
        Exercise_equipment(
            name = 'Calf Raise Machine'
        ),
        Exercise_equipment(
            name = 'None'
        )
   ]  

   # Seeding muscle groups 
   muscle_groups = [
        Muscle_group(
                name = 'Biceps'
        ),
        Muscle_group(
                name = 'Back'
        ),
        Muscle_group(
                name = 'Triceps'
        ),
        Muscle_group(
                name = 'Shoulders'
        ),
        Muscle_group(
                name = 'Chest'
        ),
        Muscle_group(
                name = 'Legs'
        ),
        Muscle_group(
                name = 'Calves'
        )
   ]

   # Seeding user stats
   user_stats = [
        User_stat(
            body_weight = 80,
            height = 178,
            user_id = 1
        ),
        User_stat(
            body_weight = 55,
            height = 162,
            user_id = 2
        ),
        User_stat(
            body_weight = 120,
            height = 170,
            user_id = 3
        )
    ]
   # session is the current session with the database 
   db.session.add_all(user_stats)
   db.session.add_all(logged_work)
   db.session.add_all(users)
   db.session.add_all(muscle_groups)
   db.session.add_all(exercise_equipments)
   db.session.add_all(exercises)
   # We need to confirm our changes and add a session commit
   db.session.commit()
   print('Tables seeded')
    