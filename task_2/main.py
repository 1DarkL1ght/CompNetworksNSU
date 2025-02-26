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


chrome_driver_path = "C:\\chromedriver-win64\\chromedriver.exe"

option = Options()
option.add_argument('--ignore-certificate-errors')
option.add_argument('--ignore-ssl-errors')

service = Service(chrome_driver_path)

browser = webdriver.Chrome(service=service, options=option)
browser.get('https://www.drom.ru/')

sign_in_buttn = browser.find_element(By.CSS_SELECTOR, "_1tt78qz3.oco7hz0")
sign_in_buttn.click()
