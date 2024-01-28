from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach" , True)

chrome = webdriver.Chrome(chrome_option)
chrome.get(url="https://www.speedtest.net/")

continue_button = chrome.find_element(By.ID, value="onetrust-accept-btn-handler")
go_button = chrome.find_element(By.CLASS_NAME, value="start-text")

try:
    continue_button.click()
finally:
    go_button.click()

new_time = time.sleep(60)

print("i am here ")
try:
    print(' i am inside try block')
    close_popup = chrome.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button')
    close_popup.click()
    time.sleep(6)
finally:
    download_speed = chrome.find_element(By.CLASS_NAME, value="result-data-large number result-data-value download-speed")
    upooad_speed = chrome.find_element(By.CLASS_NAME, value="result-data-large number result-data-value upload-speed")
    print("Download Speed :",download_speed.text)
    print("Upload Speed :",upooad_speed.text)

chrome.close()