from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/methods/1/index.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    while (result := browser.find_element(By.ID, 'result').text) == 'refresh page':
        browser.refresh()
    else:
        print(result)