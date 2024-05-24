from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://parsinger.ru/selenium/5.8/2/index.html"

with webdriver.Chrome() as driver:
    driver.get(URL)
    buttons = driver.find_elements(By.XPATH, "//input[@class='buttons']")
    for button in buttons:
        button.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        guess = driver.switch_to.alert.text
        driver.switch_to.alert.accept()
        inpt_field = driver.find_element(By.ID, "input")
        inpt_field.clear()
        inpt_field.send_keys(guess)
        check_button = driver.find_element(By.ID, "check")
        check_button.click()
        result = driver.find_element(By.ID, "result")

        if result.text != "Неверный пин-код":
            print(result.text)
            break
