from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



cookie_url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_opetions = webdriver.ChromeOptions()
chrome_opetions.add_experimental_option("detach", True)

cookie = webdriver.Chrome(options=chrome_opetions)
cookie.get(url=cookie_url)
my_cookie = cookie.find_element(By.ID, value="cookie")
my_cursor = cookie.find_element(By.ID, value="buyCursor")

def cookie_click():
    for i in range(50):
        my_cookie.click()

game = True
cursor_buy = 15
Grand_maa = 100
Factory = 500
Mine = 2000
Shipment = 7000
AlchameyLab = 50000
Portal = 1000000
time_machine = 123456789

while game:
    money = cookie.find_element(By.ID, value="money")
    cookie_click()
    if int(money.text) >= cursor_buy:
        try:
            my_cursor.click()
        finally:
            cookie_click()
    else:
        cookie_click()





cookie.close()
