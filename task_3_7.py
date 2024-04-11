import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/selenium/7/7.html")
    targets = browser.find_elements(By.TAG_NAME, 'option')

    total = sum(map(int, (i.text for i in targets)))
    input_total = browser.find_element(By.ID, "input_result")
    input_total.send_keys(str(total))
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    input()
