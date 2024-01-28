from selenium import webdriver
from selenium.webdriver.common.by import By

import requests


# header ={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Accept-Language": "en"
# }

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

canon_print_url = f"https://www.amazon.in/Canon-Pixma-G2012-Colour-Printer/dp/B07B4KHXHD/{header}"


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
# price_printer = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price_printer.text)

searchbar = driver.find_element(By.NAME, value="q")
#print(searchbar.tag_name)
#button  = driver.find_element(By.ID, value="submit")
date = driver.find_elements(By.CSS_SELECTOR, value=" .event-widget time")

print(date)

# for item in date:
#     print(item.text)

#event_names = driver.find_elements(By.CSS_SELECTOR, value=" .event-widget a")
event_names = driver.find_elements(By.CSS_SELECTOR, value=" .event-widget li a")
events = {}

for n in range(len(date)):
    events[n] = {
        "time":date[n].text,
        "name": event_names[n].text
    }

print(events)


driver.close()
