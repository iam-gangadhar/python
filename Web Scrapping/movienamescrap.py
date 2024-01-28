import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_data = response.text


data = BeautifulSoup(movie_data, "html.parser")
movie_name = data.find_all(name="h3", class_="title")

movienames = []
for movie in movie_name:
    #print(movie.text)
    movienames.append(movie.text)

#print(movienames)

movies = movienames[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        try:
            file.write(f"{movie}\n")
        except UnicodeEncodeError:
            pass
