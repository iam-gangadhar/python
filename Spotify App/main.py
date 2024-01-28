import requests
from bs4 import BeautifulSoup
import spotipy


#date = input("Enter Which Week You want Play List YYYY-MM-DD Format: ")
date = "2024-01-06"
web_url = f"https://www.billboard.com/charts/india-songs-hotw/{date}/"
print(date)
client_id ="cc4a4ad99a2f4c9a80ed15b5d2670bc0"
client_secrete="949feeee8c964482b9ad7e9639232421"




response = requests.get(url=web_url)
data_html = BeautifulSoup(response.text, "html.parser")
song = data_html.select("ul li ul li h3")
songs_list = []
for s in song:
    new_song = s.getText().strip()
    songs_list.append(new_song)

print(songs_list)