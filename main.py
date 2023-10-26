import requests, os
from datetime import datetime

#keys are stored locally for anonimity
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
SHEETY_API_KEY = os.environ['SHEETY_API_KEY']

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
AUTHORIZATION_KEY = os.environ['AUTHORIZATION_KEY']
authorization_header = {
    "Authorization": f"Bearer {AUTHORIZATION_KEY}"
}

Query = input("Name of the exercise you did: ").lower()
exercise_params = {
    "query": Query,
    "gender": "male",
    "weight_kg": 82,
    "height_cm": 191,
    "age": 20
}


response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers).json()


SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/myWorkouts/workouts"

sheety_headers = {
    "sheety-key": SHEETY_API_KEY,
}

today = datetime.now()

for exercise in range(0, len(response["exercises"])):
    name_of_exercise = response["exercises"][exercise]["name"]
    duration_mins = response["exercises"][exercise]["duration_min"]
    burned_calories = response["exercises"][exercise]["nf_calories"]

    new_row = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": name_of_exercise.title(),
            "duration": duration_mins,
            "calories": burned_calories,
        }
    }
    rsp = requests.post(url=SHEETY_ENDPOINT, json=new_row,headers=authorization_header)
    print(rsp)
