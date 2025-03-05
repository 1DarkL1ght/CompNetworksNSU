import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
# authorization code:
sign_in_buttn = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "._1tt78qz3.oco7hz0")))
sign_in_buttn.click()
print("Done!")

login_element = browser.find_element(By.ID, "sign")
login_element.send_keys('89134808098' + Keys.RETURN)

password_element = browser.find_element(By.NAME, "password")
password_element.send_keys('GeorgMax121270' + Keys.RETURN)

time.sleep(10)

sign_button = browser.find_element(By.ID, "signbutton")
sign_button.click()

time.sleep(10)'''


def main():
    pages = 5
    vehicles_data = []

    option = webdriver.ChromeOptions()
    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--ignore-ssl-errors')

    browser = webdriver.Chrome(options=option)
    browser.get('https://auto.drom.ru/')

    km_buttn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'drom.ru/auto/?distance=100')]")))
    km_buttn.click()

    for page in range(1, pages + 1):
        browser.get(f'https://novosibirsk.drom.ru/auto/page{page}/?distance=100')

        vehicles = browser.find_elements(By.CSS_SELECTOR, "[data-ftid='bulls-list_bull']")

        for vehicle in vehicles:
            title = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_title']").text
            description_items = vehicle.find_elements(By.XPATH, ".//*[@data-ftid='bull_description-item']")
            description = " ".join([item.text for item in description_items])
            price = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_price']").text
            location = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_location']").text
            date = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_date']").text

            vehicles_data.append([title, description, price, location, date])

    with open('parsed_data.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        csv_writer.writerows(vehicles_data)

    print('Saved to csv file')


main()

