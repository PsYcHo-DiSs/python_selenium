from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = 'https://parsinger.ru/infiniti_scroll_3/'

with webdriver.Chrome() as browser:
    browser.get(URL)

    for i in range(1, 6):
        div = browser.find_element(By.XPATH, f'//*[@id="scroll-container_{i}"]/div')
        for x in range(10):
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 20).perform()
            time.sleep(0.1)

    total = 0
    elements = browser.find_elements(By.XPATH, '//span[starts-with(@id, "__InfiScroll_")]')

    for element in elements:
        value = element.text
        if value.isdigit():
            total += int(value)

print(total)
