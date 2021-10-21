from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# Before testing, install chromedriver in order to proceed with the following command:
# sudo apt install chromium-chromedriver

def scrape_website(url):
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        driver.get(url)
        name = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[3]/div[1]/div[1]/h1').text
        price = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[3]/div[1]/div[2]/meta[2]').get_attribute('content')
        color = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[3]/div[2]/div[2]/span').text
        sizes = driver.find_elements(By.CLASS_NAME, 'size-unavailable')
        sizes.extend(driver.find_elements(By.CLASS_NAME, 'size-available'))
        size = [x.get_attribute('data-size') for x in sizes]
        dict = {
                'name': name,
                'price': float(price),
                'color': color,
                'size': size
        }

        return json.dumps(dict)


url = 'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99'
json = scrape_website(url)
