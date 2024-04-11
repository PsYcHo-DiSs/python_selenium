import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://parsinger.ru/selenium/3/3.html")
    each_2th_p = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    total = 0
    for elem in each_2th_p:
        total += int(elem.text)

print(total)
