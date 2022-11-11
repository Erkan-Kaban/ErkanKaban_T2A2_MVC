# T2A2 - Benchpress This API Project :muscle:

1. [Link to Trello Board](https://trello.com/b/eeVsQVj6/api-web-server-project)
2. [Github](https://github.com/Erkan-Kaban)

## Requirement 1 Identify the problem we are trying to solve by building this app.

<hr>


By creating this API, we are catering to clients that are looking for an app where they can quickly build their personalized workout routines. It aims at clients just beginning their fitness journey or even more experienced gymgoers that need help figuring out what workouts to do when they attend a gym to help users be prepared and plan on what they'll be doing when they arrive at a gym.

The app solves the problems by aiding in figuring out and planning what exercises to do with a list of workouts to choose from and adding them to their personalized list of movements, tracking what weight they've lifted and the number of repetitions, etc. That way, they can work towards bigger goals in improving their fitness and use the app to track their progress. With some apps for a beginner, it would be easier to figure out what kind of workout they will do to meet specific goals. This app helps users gain some knowledge and understanding of what body parts they want to work out, correctly categorized with the types of workouts that will help them work those body parts. This way, the users will be more confident and familiar with what they're doing when they arrive at a gym.

<hr>

## Requirement 2	Why is it a problem that needs solving?

It's a problem that needs solving because many people are just beginning and need clarification about where to start their fitness journey and require knowledge on what to do at the gym. So by helping them do this, we want to encourage them to begin attending a gym and start to help them improve their health and well-being by supporting this app we are creating.

<hr>

## Requirement 3 Why have you chosen this database system. What are the drawbacks compared to others?

I have chosen to use the postgreSQL database system, as it has the following benefits:

* It is open source meaning it is free to use and gives the user the freedom to do what they like with no copyright issues and is constantly being improved by other developers and programmers.
* Highly compatible with majority of operating systems.
* Postgreql can be expanded to use custom functions with conjunction to Python without having to convert/compile the database.
*  Conforms with the SQL standards that bigger SQL applications also follow.
* Supports several programming languages, main ones like R, Java, Javascript, Perl.
* Supports for nearly every datatype you could think of.
* Has a robust authentication and privilege management system that can be used in any organisation. 
* Easy to use and not much training is required to learn to use it.
* Low maintenance and costs for companies.

### Draw backs compared to other DB systems?

* As it's open source, it's not owned by a singular company like MySQL because of this fact. Postgresql took time to get it's reputation in line with other larger company known DB systems.
* Postgresql focuses more on compatibility and changes that are made to improve the speed of the database requires more work than MySQL.
* On some performance metrics it has shown to be slower than MySQL.

For the reasons above, mainly that Postgreql is highly flexible and is easy to install and setup as well as easy to use with the added benefit of it being free and open source, our app isn't going to be laregly reliant on performance and is going to be more reliant on the compatibility and ease of use for our simple application. Postgresql will be more than sufficient for the applcation that we will be creating and its uses.

<hr>

### Requirement 4 Identify and discuss the key functionalities and benefits of an ORM
<br>

#### <u>Key Functionality</u>

Object Relational Mapping(ORM) is a layer between the choice of programming language (Python) and a Database Management System (PostgreSQL). The layer being the ORM in between the two helps us communicate to our database through our choice of programming language, using Object Oriented Programming (OOP). Without ORM, users would need to learn how to communicate with our databases through SQL code. Having an ORM gives us that extra option and alternative solution.<br>

#### <u>Benefits of ORM</u>

 ORM's key benefit is to help programmers who do not understand SQL to communicate with the SQL database in OOP of their already known knowledge of a programming language. Some other key benefits of ORM are:

 * Productivity: ORM helps productivity as writing this code in Python, for example, would only need to be typed once and can be run multiple times to eliminate repetitive SQL code. This added productivity is also considered DRY (Don't repeat yourself)


 * Extra Security: By using ORM, we are automatically sanitizing our data, checking for any malicious behavior in the code, and preventing any breaches. ORM automatically takes care of any potential SQL injection.

 * No prior SQL knowledge is required to code ORM.

 * Added functionality like inheriting models.

 <hr>

 ### Requirement 5 Document all endpoints for your API

## User routes:
### `/users/`
 - Method: GET
 - Arguments: None
 - Description: Returns all users
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Request Body: None
 - Response Body:

 ```json
 [
  {
    "id": 1,
    "username": "Adam",
    "email": "Adam96@gmail.com",
    "is_admin": false
  },
  {
    "id": 2,
    "username": "Admin1",
    "email": "AdminMaster90@gmail.com",
    "is_admin": true
  }
]

 ```
### `/users/<int:id>/`
 - Method: GET
 - Arguments: id
 - Description: Returns specific user
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Request Body: None
 - Response Body:

 ```json
{
    "id": 3,
    "username": "Admin2",
    "email": "AdminMaster91@gmail.com",
    "is_admin": true
}
 ```
### `/users/register/`
 - Method: POST
 - Arguments: None
 - Description: Registers user
 - Authentication: None
 - Authorization: None
 - Response Body:

 ```json
{
    "id": 7,
    "username": "George",
    "email": "Costanza",
    "is_admin": false
}
 ```
### `/users/<int:id>/`
 - Method: DELETE
 - Arguments: id
 - Description: Deletes user
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Request Body: None
 - Response Body:

 ```json
{
    "message": "User Admin2 deleted successfully"
}
```
### `/users/<int:id>/`
 - Method: PUT OR PATCH
 - Arguments: id
 - Description: Updates user information
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json
{
    "id": 1,
    "username": "Adem",
    "email": "Adam96@gmail.com",
    "is_admin": false
}
```
<hr>

## Exercise Routes
### `/exercises/`
 - Method: GET
 - Arguments: None
 - Description: Gets all exercises in database.
 - Authentication: @jwt_required()
 - Authorization: None
 - Response Body:

 ```json

[
    {
        "id": 2,
        "name": "Plank",
        "muscle_group_id": 5,
        "muscle_group": {
            "name": "Chest"
        },
        "exercise_equipment_id": 11,
        "exercise_equipment": {
            "name": "None"
        }
    },
    {
        "id": 3,
        "name": "Push-up",
        "muscle_group_id": 5,
        "muscle_group": {
            "name": "Chest"
        },
        "exercise_equipment_id": 11,
        "exercise_equipment": {
            "name": "None"
        }
    }
]

```

### `/exercises/<int:id>/`
 - Method: DELETE
 - Arguments: int
 - Description: Delete selected exercise
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Response Body:

 ```json

{
    "message": "Exercise Rear Delt Flys deleted successfully"
}

```

### `/exercises/<int:id>/`
 - Method: GET
 - Arguments: int
 - Description: Returns selected exercise
 - Authentication: @jwt_required()
 - Authorization: Bearer Token
 - Response Body:

 ```json

{
    "id": 1,
    "name": "pull-up",
    "muscle_group_id": 2,
    "muscle_group": {
        "name": "Back"
    },
    "exercise_equipment_id": 11,
    "exercise_equipment": {
        "name": "None"
    }
}

```

### `/exercises/add-workout/`
 - Method: POST
 - Arguments: None
 - Description: Creates an exercise
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Response Body:

 ```json

{
    "id": 20,
    "name": "concentrated curls",
    "muscle_group_id": 1,
    "muscle_group": {
        "name": "Biceps"
    },
    "exercise_equipment_id": 1,
    "exercise_equipment": {
        "name": "Dumbbells"
    }
}

```

### `/exercises/<int:id>/`
 - Method: PUT OR PATCH
 - Arguments: id
 - Description: Updates an exercise
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Response Body:

 ```json

{
    "id": 1,
    "name": "pull-up",
    "muscle_group_id": 2,
    "muscle_group": {
        "name": "Back"
    },
    "exercise_equipment_id": 11,
    "exercise_equipment": {
        "name": "None"
    }
}

```
### `/exercises/muscle-group/<int:muscle>/`
 - Method: GET
 - Arguments: muscle
 - Description: Gets all exercises with matching argument type
 - Authentication: @jwt_required()
 - Authorization: Bearer Token 
 - Response Body:

 ```json

[
    {
        "id": 13,
        "name": "Incline Bicep Curls",
        "muscle_group_id": 1,
        "muscle_group": {
            "name": "Biceps"
        },
        "exercise_equipment_id": 2,
        "exercise_equipment": {
            "name": "Bench"
        }
    },
    {
        "id": 14,
        "name": "Hammer Curls",
        "muscle_group_id": 1,
        "muscle_group": {
            "name": "Biceps"
        },
        "exercise_equipment_id": 1,
        "exercise_equipment": {
            "name": "Dumbbells"
        }
    }
]

```
<hr>

## Auth Routes
### `/auth/login/`
 - Method: POST
 - Arguments: None
 - Description: Logs admin or user in with token
 - Authentication: @jwt_required()
 - Authorization: Bearer Token 
 - Response Body:

 ```json

{
    "email": "Adam96@gmail.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODE0NTgzOCwianRpIjoiOTZlOTEwZGItNGViOS00MTI4LWI5ZjQtOGEwZWFiMGM2NTY0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE2NjgxNDU4MzgsImV4cCI6MTY2ODIzMjIzOH0.V-g0UZwIr85ETiDUqN-J-E5-N-_0dArx_Op34dDffQk",
    "is_admin": false
}

```
<hr>

## Logged workout routes
### `/workouts/`
 - Method: GET
 - Arguments: None
 - Description: Gets all workouts from users
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Response Body:

 ```json

[
    {
        "exercise": {
            "name": "Push-up"
        },
        "exercise_id": 1,
        "reps": 10,
        "weight": 50,
        "sets": 3,
        "id": 1,
        "user_id": 1
    },
    {
        "exercise": {
            "name": "Plank"
        },
        "exercise_id": 2,
        "reps": 10,
        "weight": 20,
        "sets": 5,
        "id": 2,
        "user_id": 1
    }
]

```

### `/workouts/user/<int:user_id>/`
 - Method: GET
 - Arguments: user_id
 - Description: Gets matching user_id's workouts
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

[
    {
        "exercise": {
            "name": "Push-up"
        },
        "exercise_id": 1,
        "reps": 10,
        "weight": 50,
        "sets": 3,
        "id": 1,
        "user_id": 1
    },
    {
        "exercise": {
            "name": "Plank"
        },
        "exercise_id": 2,
        "reps": 10,
        "weight": 20,
        "sets": 5,
        "id": 2,
        "user_id": 1
    }
]

```

### `/workouts/add/user/<int:user_id>/`
 - Method: POST
 - Arguments: user_id
 - Description: Add's exercise to users workout 
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

{
    "id": 12,
    "weight": 30,
    "exercise_id": 5,
    "exercise": {
        "name": "Incline D.B Chest Press"
    },
    "reps": 12,
    "user_id": 1,
    "sets": 2
}

```

### `/user/<int:user_id>/<int:id>/`
 - Method: PUT OR PATCH
 - Arguments: user_id, id
 - Description: updates the matched user's exercise 
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

{
    "exercise": {
        "name": "pull-up"
    },
    "exercise_id": 1,
    "reps": 10,
    "weight": 50,
    "sets": 4,
    "id": 1,
    "user_id": 1
}

```

### `/workouts/delete/user/<int:user_id>/<int:id>/`
 - Method: DELETE
 - Arguments: user_id, id
 - Description: Deletes the matched user's exercise 
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

{
    "message": "Exercise id 5 deleted successfully"
}

```
<hr>

## User stats routes

### `/user-stats/`
 - Method: GET
 - Arguments: None
 - Description: Gets all user statistics
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & Admin Only
 - Response Body:

 ```json

[
    {
        "body_weight": 80,
        "user_id": 1,
        "height": 178,
        "id": 1,
        "user": {
            "username": "Adam"
        }
    },
    {
        "body_weight": 55,
        "user_id": 2,
        "height": 162,
        "id": 2,
        "user": {
            "username": "Admin1"
        }
    }
]

```

### `/user-stats/user/<int:user_id>/`
 - Method: GET
 - Arguments: None
 - Description: Gets specific user statistics
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

{
    "body_weight": 80,
    "user_id": 1,
    "height": 178,
    "id": 1,
    "user": {
        "username": "Adam"
    }
}

```

### `/user-stats/<int:user_id>/`
 - Method: DELETE
 - Arguments: user_id
 - Description: Deletes specific user_id
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

{
    "message": "User Stat id 1 deleted successfully"
}

```

### `/user-stats/user/add-stats/<int:user_id>/`
 - Method: POST
 - Arguments: user_id
 - Description: Adds user stats for a specific user
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

{
    "body_weight": 75,
    "user_id": 1,
    "height": 173,
    "id": 4,
    "user": {
        "username": "Adam"
    }
}

```

### `/user-stats/user/<int:user_id>/`
 - Method: PUT OR PATCH
 - Arguments: user_id
 - Description: updates a specific users statistic
 - Authentication: @jwt_required()
 - Authorization: Bearer Token & User Only
 - Response Body:

 ```json

{
    "body_weight": 90,
    "user_id": 1,
    "height": 178,
    "id": 1,
    "user": {
        "username": "Adam"
    }
}

```

 <hr>

 ### Requirement 6 An ERD for your app
<br>

 ![](./docs/ERD_WORKOUT.jpeg)

 <hr>

 ### Requirement 7 Detail any third party services that your app will use

 - `python-dotenv` : This package allows us to run custom configurations through a file named .flaskenv
 now we can just do flask run, and gets all the required configuration out of the .flaskenv benefit to this is
 that we can just run flask run in the console.

 - `Flask`: A light web application framework, it starts off light but can be scaled up to bigger projects and APIs.

 - `Flask_marshmallow` : A module that deserializes/serializes objects.

 - `Flask_sqlalchemy` : An extension of flask, an ORM that allows to use Python classes and code to translate into SQL.

 - `Flask_bcrypt`: Bcrypt is used for hashing/encoding passwords registered by users.

 - `Flask_jwt_extended`: JWTManager is used to produce tokens for users JSON Web Tokens (JWT), and to get tokens identity.

 - `flask.Blueprint`: Used to create shortcuts for endpoints and to have more organised code.

<hr>

 The API created will be using a BMI score calculator from a PyPI service called BMI-Score

 By importing this package into our API our users that enter their height and body weight into their user stats (optional) we will activate this into the correct format and have a calculated BMI saved into their user stats.

 link to the third party package can be found [Here](https://pypi.org/project/BMI-Score/)

 Explanation of how it will work:
- pip install bmi_score
- import by using: from bmi_score import bmi_information, bmi
- variable a = bmi(height, body_weight) <--- Saves into a the calculated bmi
- variable b = bmi_information(a) <-- Returns BMI information based on final BMI score, returns a message to let the user know for example "You're in the healthy weight range"
- return this information to our user_stats model BMI for each user, to be saved into DB.
 <hr>

 ### Requirement 8 Describe your projects models in terms of the relationships they have with each other

### One (and only one) to many from the following two models to exercises model:
 - MUSCLE_GROUPS(id, name)
 - EXERCISE_EQUIPMENT(id, name)

    - With these two models, we have one and only one-to-many relationships with the exercises model. Therefore, each muscle group and exercise equipment used will be listed in the exercise entity many times and only once from each muscle group and exercise equipment in every instance. This way we can easily identify the equipment used and muscle groups for each exercise listed in exercises.

### Zero or one to one or many from exercises to user_workout_template model:
- USER_WORKOUT_TEMPLATE(id, exercise_ID, user_ID)
    - We have the option to add an exercise. Once we have decided to add a list of exercises to our user_workout_template, the id from exercises can appear one or many times in the template model.

### One (and only one) from users to user_workout_template model:
-   USERS(id, f_name, l_name, email, password, is_admin) 
    - One and only one user is sent out to our worker template so we can pair up the user with he/she work out template. 

### Zero or one to Zero or one relationship between users and user_stats model:  
-   USER_STATS(id, body_weight, height, BMI, user_ID)
    - With this relationship we have both ends as optional for user and user stats relationship to be created. I made it optional for the user rather than mandatory as it's more user friendly if they didn't feel like they didn't need to input their personal details.

### One to many relationship between user_workout_template and user_workout_log_history:
- USER_WORKOUT_LOG_HISTORY(user_template_id_logged_workout_id, user_workout_template_id, logged_id, date_logged)
    - Once a user creates a workout template, we want to have one instance sent to a join table user_workout_log_history that could save many templates, so that is why there are many relationships on that end of the model.

### Zero or many to one (and only one) relationship between user_workout_log_history and logged_workout
- LOGGED_WORKOUT(id, sets, reps, weight, calories_burnt)
 - Once the user has logged a workout template I wanted this information to be tied in with the join table. a logged workout would be only one but can result and show many times in a log history of workouts.
 <hr>

 ### Requirement 9 Discuss the database relations to be implemented in your application

 -

 <hr>

 ### Requirement 10 Describe the way tasks are allocated and tracked in your project

 The tasks are allocated and tracked in my project by the use of the Trello board. I split the project into stages:

 - Stages:
    - Stage 1: Includes documentation, prioritizing requirements in the project, and colored to keep track of how it's all coming together as well as due dates to ensure I keep track of deadlines.
    - Stage 1.5: The planning side of things is similar to documentation, so I called it 1.5. It involves the planning aspect, such as ERD creation.
    - Stage 2: This stage involves the actions required for the documentation and planning. It includes cards to put everything together.
    - Stage 3: List any extra final stage polishes required to complete the project, including documenting the endpoints and things that need to come in the later stages.

- Misc List:
    - In Progress:
        - I decided to drag what's currently in progress but drag them back to their respective stage list when complete with a tick to know where they belong and completion.
    - Trello Checkups & Daily stand ups
        - Made a checklist to ensure that I've completed the daily trello & standup checkups.
- Also an in progress list was created so that I can keep track of what was to be completed next.
 
The project also prioritizes each card in colors that signify its importance:

- Color coordination: 
    - green: priority Low
    - orange: priority Medium
    - red: priority High

As the project progresses, I will update and possibly create new cards if any extra obstacles arise. However, this is my current Software Development Plan (SDP), and I will be making extra additions to any changes from here.

![](./docs/trello_board.jpg)




