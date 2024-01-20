import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 94.50
HEIGHT_CM = 172
AGE = 33

APP_ID = "0eca5188"
API_KEY = "81dacc75608dceebd9b74c8e48827e4f"

#Documentation part for Calling API https://developer.syndigo.com/docs/nutritionix-api-guide

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
data = response.json()

date = datetime.today()
today_date = date.strftime('%d/%m/%Y')
time = datetime.now()
current_time = time.strftime('%H:%M')

# Workout Details Catching
exercise = data['exercises'][0]['name']
duration = data['exercises'][0]['duration_min']
calories = round(data['exercises'][0]['nf_calories'])


workout = {
    'workout':{
        'date': today_date,
        'time': current_time,
        'exercise' : exercise,
        'duration': duration,
        'calories':calories,
        #'id': 3
    }
}

print(workout)



# Sheety Using to update the data in Google Sheets
# https://api.sheety.co/username/projectName/sheetName

#sheety_read_data = "https://api.sheety.co/c963b0bd995c7c39301d975a0ec1237d/myWorkouts2024/workouts"
#response = requests.get(url=sheety_read_data)
#print(response.json())

# Using Authentication in Sheety
sheety_update_data = "https://api.sheety.co/c963b0bd995c7c39301d975a0ec1237d/myWorkouts2024/workouts"

sheet_response = requests.post(sheety_update_data, json=workout, auth=('gangadhar', 'al;sjflksd;ahjklasd'))

# Bearer Authentication using Token
# bearer_headers = {
# "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(sheety_update_data, json=workout, headers=bearer_headers)

my_data = sheet_response.json()
print(my_data)


#response_post = requests.post(url=sheety_update_data, json=workout)
#chekcing = response_post.json()
