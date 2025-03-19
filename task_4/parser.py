import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


option = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=option)


def load_page():
    browser.get('https://auto.drom.ru/')

    km_buttn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'drom.ru/auto/?distance=100')]")))
    km_buttn.click()


def parse_pages(pages):
    vehicles_data = []

    for page in range(1, pages + 1):
        browser.get(f'https://novosibirsk.drom.ru/auto/page{page}/?distance=100')

        vehicles = browser.find_elements(By.CSS_SELECTOR, "[data-ftid='bulls-list_bull']")

        for vehicle in vehicles:
            name, year = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_title']").text.split(", ")
            description_items = vehicle.find_elements(By.XPATH, ".//*[@data-ftid='bull_description-item']")
            description = " ".join([item.text for item in description_items])
            price = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_price']").text
            location = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_location']").text
            date = vehicle.find_element(By.CSS_SELECTOR, "[data-ftid='bull_date']").text

            vehicles_data.append([name, year, description, price, location, date])

    return vehicles_data


def save_to_csv(filename, vehicles_data):
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        csv_writer.writerows(vehicles_data)

    print('Saved to csv file')


def run_parser(num_pages=1, filename='parsed_data.csv'):
    filename = 'parsed_data.csv'

    option.add_argument('--ignore-certificate-errors')
    option.add_argument('--ignore-ssl-errors')

    load_page()
    vehicles_data = parse_pages(num_pages)
    save_to_csv(filename, vehicles_data)


# main()
