import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hkasfjal3j13049fasfjl13254r"
USERNAME = "ganga4cs"

users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# creating User using post request
# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Documentation please read this https://docs.pixe.la/entry/post-graph

graph_config = {
    "id": "graph2",
    "name": "Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Posting the data using Post method

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2"
#update_endpoint = f"https://pixe.la/v1/{USERNAME}/graphs/graph2"

update_graph = {
    "date": "20240119",
    "quantity":"1.30"}

# update_response = requests.post(url=update_endpoint, json=update_graph, headers=headers)
# print(update_response.text)

dateofbirth = datetime(year=1989,month=5,day=25)
print(dateofbirth)
print(dateofbirth.day)
