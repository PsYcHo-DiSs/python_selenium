from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/scroll/4/index.html'

with webdriver.Chrome() as webdriver:
    webdriver.get(URL)

    elements = webdriver.find_elements(By.CLASS_NAME, 'btn')
    unique = 0
    for elem in elements:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", elem)
        elem.click()
        unique += int(webdriver.find_element(By.ID, 'result').text)

    print(unique)
