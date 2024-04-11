import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'form')
    for elem in input_form:
        elem.send_keys('Text')

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    time.sleep(5)
