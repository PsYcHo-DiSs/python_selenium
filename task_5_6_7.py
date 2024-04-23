from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://parsinger.ru/selenium/5.5/3/1.html'

with webdriver.Chrome() as driver:
    driver.get(URL)

    textareas = driver.find_elements(By.CSS_SELECTOR, '.parent textarea')
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '.parent input[type="checkbox"]')

    total_sum = 0

    for textarea, checkbox in zip(textareas, checkboxes):
        if checkbox.is_selected():
            value = int(textarea.get_attribute('value'))
            total_sum += value

    print("Общая сумма:", total_sum)
    