from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/methods/5/index.html'

with webdriver.Chrome() as webdriver:
    webdriver.get(URL)
    links = [item.get_attribute('href') for item in webdriver.find_elements(By.TAG_NAME, 'a')]

    max_expiry = 0
    for link in links:
        webdriver.get(link)
        cookies = webdriver.get_cookies()
        for cookie in cookies:
            if cookie['expiry'] > max_expiry:
                max_expiry = cookie['expiry']
                max_expiry_link = link

    webdriver.get(max_expiry_link)

    answer = webdriver.find_element(By.ID, 'result')
    print(answer.text)
