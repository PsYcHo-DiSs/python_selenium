import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/4/4.html")
    check_boxes = browser.find_elements(By.CLASS_NAME, "check")

    for box in check_boxes:
        box.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    result = browser.find_element(By.ID, "result").text
    time.sleep(5)
    print(result)
