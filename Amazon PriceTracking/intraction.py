from selenium import webdriver
from selenium.webdriver.common.by import By

#intraction with wikipedia getting the number of articales count

# keep chrome browser open after Program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", False)

# Create and configure the Chrome Driver
wikipedia = webdriver.Chrome(options=chrome_options)

# Navigating any Website using Webdriver Object in Selenium we are using get method
wikipedia.get(url="https://en.wikipedia.org/wiki/Main_Page")

# Getting Total count value using ID tag
total_count = wikipedia.find_element(By.ID, value="articlecount")

# Split method used to split the text
my_data = total_count.text.split()
print(my_data[0])

# Second way of Collect
count = wikipedia.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(count.text)


# Finding Elements by Link Text
link_text = wikipedia.find_element(By.LINK_TEXT, value="Content portals")
print(link_text.text)
# calling click even to click the text
link_text.click()







wikipedia.close()