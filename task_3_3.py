import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    time.sleep(2)
    elements = browser.find_elements(By.XPATH, '//div[@class="text"]/p')
    total = 0

    for elem in elements:
        total += int(elem.text)


print(total)
