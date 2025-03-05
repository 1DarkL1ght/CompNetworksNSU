from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# chrome_driver_path = "C:\\chromedriver-win64\\chromedriver.exe"

option = Options()
option.add_argument('--ignore-certificate-errors')
option.add_argument('--ignore-ssl-errors')

# service = Service(chrome_driver_path)

browser = webdriver.Chrome(options=option)
browser.get('https://auto.drom.ru/')

# sign_in_buttn = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "._1tt78qz3.oco7hz0")))
# sign_in_buttn.click()
# print("Done!")

# login_element = browser.find_element(By.NAME, "sign")
# login_element.send_keys('89134808098' + Keys.RETURN)

# password_element = browser.find_element(By.NAME, "password")
# password_element.send_keys('GeorgMax121270' + Keys.RETURN)

# time.sleep(10)

# sign_button = browser.find_element(By.ID, "signbutton")
# sign_button.click()

# time.sleep(10)


vehicles = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "css-1f68fiz.ea1vuk60")))
print(vehicles)
time.sleep(5)