from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://parsinger.ru/selenium/5.7/1/index.html"

with webdriver.Chrome() as driver:
    driver.get(URL)
    data = driver.find_elements(By.CSS_SELECTOR, '.button-container .clickMe')
    for button in data:
        driver.execute_script("return arguments[0].scrollIntoView(true);", button)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button)).click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = driver.switch_to.alert.text
    print(alert_text)
