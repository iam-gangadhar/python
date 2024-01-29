import requests


# name = "gangadhar" #input("Enter your name ?")
# response = requests.get(url=f"https://api.agify.io?name={name}")
# gender = requests.get(url=f"https://api.genderize.io?name={name}")
#
# name_dictionary = response.json()
# gender_dictionary = gender.json()
#
# print(name_dictionary["age"])

my_data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
data = my_data.json()
print(data)