import requests
from bs4 import BeautifulSoup
import lxml

header ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en"
}


printer_url = "https://www.amazon.in/Canon-Pixma-G2012-Colour-Printer/"
response = requests.get(url=printer_url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen")
print(price)

# price not getting from beautiful soup search in internet
