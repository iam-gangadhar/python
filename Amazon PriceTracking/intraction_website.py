from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from python.Pomodoro_Python.main import window

chrome_opetions = webdriver.ChromeOptions()
chrome_opetions.add_experimental_option("detach", True)

chrome = webdriver.Chrome(chrome_opetions)
chrome.get(url="https://secure-retreat-92358.herokuapp.com/")

fname = chrome.find_element(By.NAME, value="fName")
lname = chrome.find_element(By.NAME, value='lName')
email = chrome.find_element(By.NAME, value="email")

fname.send_keys("Gangadhar")
lname.send_keys("helloworld")
email.send_keys("helloworld@gmail.com")
button = chrome.find_element(By.TAG_NAME, value="button")
button.click()



chrome.close()
