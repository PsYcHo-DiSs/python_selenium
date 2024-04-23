from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://parsinger.ru/selenium/5.5/1/1.html'

with webdriver.Chrome() as browser:
    browser.get(URL)
    targets = browser.find_elements(By.CLASS_NAME, 'text-field')
    for elem in targets:
        elem.clear()

    button = browser.find_element(By.ID, 'checkButton')
    button.click()

    # Ждем появления алерта
    WebDriverWait(browser, 5).until(EC.alert_is_present())

    # Переключаемся на алерт
    alert = browser.switch_to.alert

    # Получаем текст из алерта
    alert_text = alert.text

    # Выводим текст алерта для проверки
    print(alert_text)

    # Закрываем алерт
    alert.accept()