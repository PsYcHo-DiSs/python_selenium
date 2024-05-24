from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://parsinger.ru/selenium/5.8/1/index.html"

with webdriver.Chrome() as driver:
    driver.get(URL)
    buttons = driver.find_elements(By.XPATH, "//input[@class='buttons']")
    for button in buttons:
        button.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        try:
            result = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "result")))
            if result.text:
                print(result.text)
                break
        except:
            continue
