from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = 'https://parsinger.ru/infiniti_scroll_2/'

with webdriver.Chrome() as browser:
    browser.get(URL)

    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 10).perform()
        time.sleep(0.1)

    elements = browser.find_elements(By.XPATH, '//p[starts-with(@id, "__InfiScroll_")]')

    total = 0
    for element in elements:
        value = element.text
        if value.isdigit():
            total += int(value)

    print(total)
