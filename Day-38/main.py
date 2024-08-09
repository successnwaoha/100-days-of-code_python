import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "185"
AGE = "17"

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
BEARER_TOKEN = "sdfghjnwe45rt6yuiSDFGHJK456TYU"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ad99b3b39230f295fbc8127f314e8ac9/workoutTracking/workouts"

exercise_text = input("Tell me which exrecises you did: ")

parameters = {
    "query" : exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }
    
    bearer_headers = {
        "Authorization" : f"Bearer {BEARER_TOKEN}"
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)