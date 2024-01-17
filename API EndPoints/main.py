import requests

MY_LAT = 17.385044
MY_LONG = 78.486671

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# status = response.raise_for_status()
# data = response.json()
# print(status)
# print(data["iss_position"])
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# position = (longitude,latitude)
# print(position)


# kany = requests.get("https://api.kanye.rest/")
# quote = kany.json()
# print(quote["quote"])

# setting our location to know the sunrise and sunset in our area
parameter = {
    "lat": MY_LAT,
    "lang": MY_LONG
}
response_2 = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}")
sun_data = response_2.json()
print(response_2.raise_for_status())
print(sun_data)