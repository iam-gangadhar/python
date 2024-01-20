import requests

APIkey ="55b9fa20a28f207703dce6d1b2514105"
lat = 17.4065
lon = 78.4772
#----------------------------------------------------------------------------------------
#  Twilio SMS Code
# ------------------------------------------------------------------------------------------
from twilio.rest import Client

account_sid = 'AC1e9485c29cb339a95f39eb95c7916ac4'
auth_token = "6f750566d10e351a227e39187799e6c3"

client = Client(account_sid, auth_token)
message = client.messages.create(
  from_='+13606394140',
  to='+918125351431'
)

print(message.sid)









#---------------------------------------------------------------

#MY_16DAYS = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={APIkey}"
MY_ONEDAY_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}"
MY_FIVE_DAYS_FORECAST = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APIkey}"

response = requests.get(url=MY_FIVE_DAYS_FORECAST)
weather_data = response.json()
#print(response.raise_for_status())
#MY_DATA = weather_data["list"][0]["weather"][0]["id"]
n = 8
for day in range(5):
    MY_DATA = weather_data["list"][n-1]["weather"][0]["id"]
    n +=8
    if MY_DATA <= 700:
        print("PLease Bring Umberalla")
    else:
        print("SKY IS Clear... Hapy VISIT OUTSIDE")
