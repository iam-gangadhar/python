import requests
from bs4 import BeautifulSoup
#response = requests.get(url="https://news.ycombinator.com/")
eenadu = requests.get(url="https://www.eenadu.net/")


# print(response.raise_for_status())
# print(response.text)


# web_page = response.text
# soup = BeautifulSoup(web_page, "html.parser")
# #print(soup.title)
# artical_tag = soup.find(name="span", class_="titleline")
# print(artical_tag.get("href"))

data = BeautifulSoup(eenadu, "html.parser")
print(data)