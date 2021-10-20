from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def scrape_website(url):
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        driver.get(url)
        dict = {}
        dict['name'] = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[3]/div[1]/div[1]/h1').text
        dict['price'] = float(driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[3]/div[1]/div[2]/meta[2]').get_attribute('content'))
        dict['color'] = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[3]/div[2]/div[2]/span').text
        sizes = driver.find_elements(By.CLASS_NAME, 'size-unavailable')
        sizes.extend(driver.find_elements(By.CLASS_NAME, 'size-available'))
        dict['size'] = [x.get_attribute('data-size') for x in sizes]

        return json.dumps(dict)


url = 'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99'
json = scrape_website(url)
