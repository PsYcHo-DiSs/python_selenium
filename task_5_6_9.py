import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://parsinger.ru/selenium/5.5/5/1.html'

driver = webdriver.Chrome()
driver.get(URL)
wait = WebDriverWait(driver, 10)

containers = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@id="main-container"]/div')))

for container in containers:
    hex_color = container.find_element(By.TAG_NAME, 'span').text

    select_element = container.find_element(By.TAG_NAME, 'select')
    select_element.click()
    select_element.find_element(By.CSS_SELECTOR, f'option[value="{hex_color}"]').click()  # Выбираем нужный цвет

    button = container.find_element(By.CSS_SELECTOR, f'button[data-hex="{hex_color}"]')
    button.click()

    checkbox = container.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    checkbox.click()

    text_field = container.find_element(By.CSS_SELECTOR, 'input[type="text"]')

    text_field.clear()
    text_field.send_keys(hex_color)

    check_button = container.find_element(By.XPATH, './/button[text()="Проверить"]')
    check_button.click()

    time.sleep(2)

text_fields_filled = all(
    container.find_element(By.CSS_SELECTOR, 'input[type="text"]').get_attribute('value') != '' for container in
    containers)

if text_fields_filled:
    check_all_button = driver.find_element(By.CSS_SELECTOR, 'body > button')
    check_all_button.click()

    try:
        alert = wait.until(EC.alert_is_present())
        print(alert.text)
        alert.accept()
    except:
        print("Алерт не найден")
else:
    print("Не все поля заполнены")

driver.quit()
