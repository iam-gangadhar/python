import requests


name = "gangadhar" #input("Enter your name ?")
response = requests.get(url=f"https://api.agify.io?name={name}")
gender = requests.get(url=f"https://api.genderize.io?name={name}")

name_dictionary = response.json()
gender_dictionary = gender.json()

print(name_dictionary["age"])

