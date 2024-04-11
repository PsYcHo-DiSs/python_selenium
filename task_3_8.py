import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def f():
    return str(((12434107696 * 3) * 2) + 1)


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/6/6.html")
    targets = browser.find_elements(By.TAG_NAME, 'option')
    for option in targets:
        if option.text == f():
            option.click()
            break

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    input()