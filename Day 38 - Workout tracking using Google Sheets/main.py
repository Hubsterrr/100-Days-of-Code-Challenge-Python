import requests
import datetime as dt
import os


app_id = os.environ.get("APP_ID")
api_key = os.environ.get("API_KEY")
sheety_token = os.environ.get("SHEETY_TOKEN")


query = input("Tell me which exercises you did today: ")


nutritionix_headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

sheety_headers = {
        "Authorization": sheety_token
    }

parameters = {
    "query": query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

date = dt.datetime.now()
date_format = date.strftime("%m/%d/%Y")
time_format = date.strftime("%H:%M:%S")

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=nutritionix_headers)
response.raise_for_status()
exercise_list = response.json()["exercises"]

for workout in exercise_list:
    sheety_input = {
        "workout": {
                "date": date_format,
                "time": time_format,
                "exercise": workout["name"],
                "duration": workout["duration_min"],
                "calories": workout["nf_calories"],

            }

    }
    response = requests.post(url="https://api.sheety.co/e3c04c44689f6e1dbab65cb8ab4e1ac1/myWorkouts/workouts", json=sheety_input, headers=sheety_headers)
    response.raise_for_status()
    print(response.text)

# link to google sheet where the data is uploaded:
# https://docs.google.com/spreadsheets/d/1Lp4NnmqGSuAjX9T9hikjW4Fp2Pk4ibhak-mo0LUSRnQ/edit#gid=0

