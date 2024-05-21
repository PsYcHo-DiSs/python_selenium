from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = "https://parsinger.ru/selenium/5.7/5/index.html"

with webdriver.Chrome() as driver:
    driver.get(URL)
    buttons = driver.find_elements(By.XPATH, "//button[@class='timer_button']")
    for button in buttons:
        hold_time = float(button.text)
        action = ActionChains(driver)
        action.click_and_hold(button).pause(hold_time).release(button).perform()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = driver.switch_to.alert.text
    print(alert_text)
