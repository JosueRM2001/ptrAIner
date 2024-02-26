import os
from openai import OpenAI
from src.nlp.utils.Const import TEMPERATURE, MAX_TOKENS, CLEAN_TEXT
from config.config import routineCollection
from bson import ObjectId

class InferenceService:
    def __init__(self):
        self.__model = os.getenv('OPENAI_MODEL', 'text-davinci-003')
        self.__openai_client = OpenAI()
        self.__text = ""
        self.__prompt_template = 'you are an expert in sports coaching and you are gonna give me a '
        self.__prompt_template_example = 'Example input: preference = strenght training, objective = build muscle, distribution = push, volume = Max adaptative volume. Example answer: Exercise template: Exercise: bench press | sets_number: 4'

    def __inference(self, prompt):
        return CLEAN_TEXT(self.__openai_client.completions.create(
            model=self.__model,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        ).choices[0].text)

    def invokeRecomendation(self, preference: str, objective: str, distribution: str, volume: str) -> str:
        prompt = (self.__prompt_template) + preference + " routine to " + objective + " for: " + distribution + " using a volume of " + volume + " answering only the exercise and the number of sets per exercise. Following the Exercise template: " + self.__prompt_template_example
        return self.__inference(prompt)

    def saveRoutineInDB(user_id: int, routine_name: str):
        routine = {
            "user_id": user_id,
            "routine_name": routine_name
        }
        result = routineCollection.insert_one(routine)
        inserted_id = result.inserted_id
        return inserted_id

    def saveExerciseInRoutineInDB(id: str, exercise_name: str, total_sets: int):
        exercise = {
            "exercise_name": exercise_name,
            "total_sets": total_sets
        }
        routineCollection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$addToSet": {"exercise": (exercise)}}

        )