from bs4 import BeautifulSoup
import requests


google_form = "https://docs.google.com/forms/d/e/1FAIpQLSdBNk5fsRO6R9uqxQtcadvfLnFDyM_DD4f2WY4IMGGAKRoilw/viewform"
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
web_data = response.text

data = BeautifulSoup(web_data, "html.parser")
link = data.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
price = data.find_all(name="div", class_="PropertyCardWrapper")


property_links = []
property_address = []
property_price = []

for p in price:
    p_data = p.get_text().rstrip().lstrip()
    new_price = p_data[:6]
    property_price.append(new_price)

for item in link:
    address = item.text.lstrip().rstrip()
    p_link = item.get("href")
    property_address.append(address)
    property_links.append(p_link)

print(len(property_address))
print(len(property_price))
print(len(property_links))

# ------------------------------------------------------------------------------------------
#  using selenium to update the data
# -----------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_opetions = webdriver.ChromeOptions()
chrome_opetions.add_experimental_option("detach", True)

gform = webdriver.Chrome(chrome_opetions)
gform.get(url=google_form)

# address_input = gform.find_element(By.CLASS_NAME, value="whsOnd.zHQkBf")
# price_property = gform.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# link_input = gform.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
# submit_form = gform.find_element(By.CLASS_NAME, value='NPEfkd.RveJvd.snByac')





for i in range(len(property_links)):
    gform.get(url=google_form)
    time.sleep(2)

    address = gform.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/'
                                                 'div[1]/div/div[1]/input')
    price = gform.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/'
                                               'div[1]/div/div[1]/input')
    link = gform.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div'
                                              '/div[1]/div/div[1]/input')

    submit_button = gform.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]'
                                                       '/div[1]/div/span/span')

    address.send_keys(property_address[i])
    price.send_keys(property_price[i])
    link.send_keys(property_links[i])
    time.sleep(1)
    submit_button.click()
    time.sleep(2)





gform.close()

