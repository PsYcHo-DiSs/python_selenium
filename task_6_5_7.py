from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

URL = "https://parsinger.ru/selenium/5.7/4/index.html"

with webdriver.Chrome() as driver:
    driver.get(URL)

    container = driver.find_element(By.ID, 'main_container')
    for _ in range(100):
        driver.execute_script("arguments[0].scrollTop += 100;", container)
        time.sleep(0.1)

    child_containers = driver.find_elements(By.CSS_SELECTOR, ".child_container input[type='checkbox']")
    for checkbox in child_containers:
        if not int(checkbox.get_attribute("value")) % 2:
            checkbox.click()

    alert_button = driver.find_element(By.CLASS_NAME, 'alert_button')
    alert_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = driver.switch_to.alert.text
    print(alert_text)
