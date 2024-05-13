from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://parsinger.ru/scroll/2/index.html"

with webdriver.Chrome() as driver:
    driver.get(URL)

    total = 0
    for i in range(1, 101):
        checkbox_id = str(i)
        checkbox = driver.find_element(By.ID, checkbox_id)
        checkbox.click()
        time.sleep(0.1)
        span_id = "result" + str(i)
        span_text = driver.find_element(By.ID, span_id)
        if span_text.text:
            span_text = int(span_text.text)
            total += span_text

    print(total)
