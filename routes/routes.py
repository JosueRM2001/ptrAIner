from fastapi import APIRouter
from config.config import routineCollection
from bson import ObjectId
from bson.json_util import dumps
import json
from dotenv import load_dotenv
from src.nlp.service.InferenceService import InferenceService
import requests
from src.DB_Connection.service.Connection_Service import Connection_Service as cs
from src.Calculations.Calculations_Service import Calculations_Service as calculations


endPoints = APIRouter()

@endPoints.get("/")
def home():
    return {
        "status": "Ok",
        "message": "My first API is running"
    }

@endPoints.get("/recomendate/routine")
def recomendate(userName: str, preference: str, distribution: str, volume: str):
    load_dotenv("secrets/.env")
    objective = cs.get_objective(userName)
    recomendation = str(InferenceService().invokeRecomendation(preference, objective, distribution, volume))
    recomendation_dict = {}
    recomendation_list = recomendation.split(" Exercise: ")
    userId = cs.get_id(userName)[0]
    routine_id = InferenceService.saveRoutineInDB(userId, distribution)
    for exercise in recomendation_list[1:]:
        name, sets = exercise.split(" | sets_number: ")
        recomendation_dict[name] = int(sets)
        InferenceService.saveExerciseInRoutineInDB(routine_id, name, sets)
        print(name, " : ", sets)
    return {
        "recomendation": json.loads(json.dumps(recomendation_dict, indent=4))
    }

@endPoints.get("/user")
def getUser(username: str):
    id = cs.get_id(username)[0]
    height = cs.get_height(username)
    weight = cs.get_weight(username)
    age = cs.get_age(username)
    genre = cs.get_genre(username)
    activity_factor = cs.get_activity_factor(username)
    objective = cs.get_objective(username)
    neck = cs.get_neck(username)
    waist = cs.get_waist(username)
    hip = cs.get_hip(username)
    maintenance_calories = cs.get_maintenance_calories(username)
    objective_calories = cs.get_objective_calories(username)
    body_fat = cs.get_body_fat(username)
    hidratation = cs.get_hidratation(username)
    protein = cs.get_protein(username)
    carbs = cs.get_carbs(username)
    fat = cs.get_fat(username)
    return {
        'id': id,
        'username': username,
        'height': height,
        'weight': weight,
        'age': age,
        'genre': genre,
        'activity_factor': activity_factor,
        'objective': objective,
        'maintenance_calories': maintenance_calories,
        'objective_calories': objective_calories,
        'hidratation': hidratation,
        'neck': neck,
        'waist': waist,
        'hip': hip,
        'body_fat': body_fat,
        'protein': protein,
        'carbs': carbs,
        'fat': fat
    }
@endPoints.get("/user/routines")
def getAllUserRoutines(username : str):
    user_id = cs.get_id(username)[0]
    routines = routineCollection.find({"user_id": user_id})
    convertedRoutines = json.loads(dumps(routines))
    '''for routine in convertedRoutines:
        if "_id" in routine:
            print(f"ID: {routine['_id']['$oid']}")
        if "user_id" in routine:
            print(f"User ID: {routine['user_id']}")
        if "routine_name" in routine:
            print(f"Routine's name: {routine['routine_name']}")
        if "exercise" in routine:
            for exercise in routine["exercise"]:
                if "exercise_name" in exercise:
                    print(f"Exercise: {exercise['exercise_name']}")
                if "objective_muscle" in exercise:
                    print(f"Objective Muscle: {exercise['objective_muscle']}")
                if "total_sets" in exercise:
                    print(f"Sets: {exercise['total_sets']}")
                if "set" in exercise:
                    for set in exercise["set"]:
                        if "set_number" in set:
                            print(f"Set Number: {set['set_number']}")
                        if "method" in set:
                            print(f"Set Method: {set['method']}")
                        if "done" in set:
                            print(f"Set done: {set['done']}")
                        if "rep" in set:
                            for rep in set["rep"]:
                                if "weight" in rep:
                                    print(f"Weight: {rep['weight']}")
                                if "reps_number" in rep:
                                    print(f"Reps number: {rep['reps_number']}")
                                if "partials" in rep:
                                    print(f"Partials: {rep['partials']}")'''
    return convertedRoutines


@endPoints.post("/login")
def login(username: str, password: str):
    url = "http://192.168.100.93:90/api/auth/login"
    data = {"username": username, "password": password}
    response = requests.api.post(url, json=data)
    if response.status_code == 200:
        log = json.loads(response.content.decode('utf-8'))
        return {
            'Message': log['accessToken']
        }
    else:
        return {
            'Message': 'Unauthorized'
        }

@endPoints.post("/register")
def register(username: str, password: str):
    url = "http://192.168.100.93:90/api/auth/register"
    data = {"username": username, "password": password}
    response = requests.api.post(url, json=data)
    if response.status_code == 200:
        return login(username, password)
    else:
        return {
            'Message': 'Unable'
        }


@endPoints.post("/id")
def getUseId(username: str):
    sessions = cs.get_id(username)
    log = int(sessions[0])
    return log

@endPoints.patch("/survey")
def fillSurvey(username: str, height: float, weight: float, age: int, genre: str, activity_factor: str, objective: str, neck: float, waist: float, hip: float):
    if cs.confirm_user(username):
        cs.fill_survey(username, height, weight, age, genre, activity_factor, objective, neck, waist, hip)
        maintenance_calories = calculations.get_calories(weight, height, age, activity_factor, genre)
        objective_calories = calculations.get_calories_by_objective(maintenance_calories, objective)
        body_fat = calculations.get_body_fat_percent(height, neck, waist, hip, genre)
        hidratation = round(calculations.get_hidratation_by_activity_factor(height, weight, age, genre, activity_factor) / 1000, 2)
        protein = calculations.get_macros(weight, activity_factor, objective_calories)[0]
        carbs = calculations.get_macros(weight, activity_factor, objective_calories)[1]
        fat = calculations.get_macros(weight, activity_factor, objective_calories)[2]
        cs.update_maintenance_calories(username, maintenance_calories)
        cs.update_objective_calories(username, objective_calories)
        cs.update_fat_percent(username, body_fat)
        cs.update_hidratation(username, hidratation)
        cs.update_protein(username, protein)
        cs.update_carbs(username, carbs)
        cs.update_fat(username, fat)
        return {
            'Message': 'User survey saved'
        }
    else:
        return {
            'Message': "User doesn't exists"
        }

@endPoints.get("/survey/calculations")
def getCalculations(username: str):
    height = cs.get_height(username)
    weight = cs.get_weight(username)
    age = cs.get_age(username)
    genre = cs.get_genre(username)
    activity_factor = cs.get_activity_factor(username)
    objective = cs.get_objective(username)
    neck = cs.get_neck(username)
    waist = cs.get_waist(username)
    hip = cs.get_hip(username)
    maintenance_calories = calculations.get_calories(weight, height, age, activity_factor, genre)
    objective_calories = calculations.get_calories_by_objective(maintenance_calories, objective)
    body_fat = calculations.get_body_fat_percent(height, neck, waist, hip, genre)
    hidratation = round(calculations.get_hidratation_by_activity_factor(height, weight, age, genre, activity_factor) /1000 , 2)
    protein = calculations.get_macros(weight, activity_factor, objective_calories)[0]
    carbs = calculations.get_macros(weight, activity_factor, objective_calories)[1]
    fat = calculations.get_macros(weight, activity_factor, objective_calories)[2]
    cs.update_maintenance_calories(username, maintenance_calories)
    cs.update_objective_calories(username, objective_calories)
    cs.update_fat_percent(username, body_fat)
    cs.update_hidratation(username, hidratation)
    cs.update_protein(username, protein)
    cs.update_carbs(username, carbs)
    cs.update_fat(username, fat)
    return {
        "Message": "Successfully updated"
    }

@endPoints.post("/new/routine")
def newRoutine(user_id: int, routine_name: str):
    routine = {
        "user_id": user_id,
        "routine_name": routine_name
    }
    routineCollection.insert_one(routine)
    return {
        "status": "Ok",
        "message": "Data inserted"
    }
@endPoints.patch("/add/exercise/${id}")
def addExerciseToRoutine(id: str, exercise_name: str, objective_muscle: str, total_sets: int):
    exercise = {
        "exercise_name": exercise_name,
        "objective_muscle": objective_muscle,
        "total_sets": total_sets
    }
    routineCollection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$addToSet": {"exercise": (exercise)}}

    )
    return {
        "status": "Ok",
        "message": "Exercise added to routine"
    }

@endPoints.patch("/add/set/${id}/${exercise_name}")
def addSetToExercise(id: str, exercise_name: str, set_number: int, method: str, done: bool):
    set = {
        "set_number": set_number,
        "method": method,
        "done": done
    }
    routineCollection.find_one_and_update({"_id": ObjectId(id), "exercise.exercise_name": exercise_name},
                                              {"$addToSet": {"exercise.$.set": (set)}})
    return {
        "status": "Ok",
        "message": "Set added to exercise"
    }

@endPoints.patch("/add/rep/${id}/${exercise_name}/${set_number}")
def addRepToSet(id: str, exercise_name: str, set_number: int, weight: float, reps_number: int, partials: bool):
    rep = {
        "weight": weight,
        "reps_number": reps_number,
        "partials": partials
    }
    routineCollection.update_one({"_id": ObjectId(id), "exercise.exercise_name": exercise_name, "exercise.set.set_number": set_number},
                                 {"$push": {"exercise.$.set.$[elem].rep": (rep)}},
                                 array_filters=[{"elem.set_number": 1}])
    return {
        "status": "Ok",
        "message": "Rep added to set"
    }
@endPoints.get("/all/routines")
def getAllRoutines():
    routines = routineCollection.find()
    convertedRoutines = json.loads(dumps(routines))
    return {
        "status": "Ok",
        "data": convertedRoutines
    }
