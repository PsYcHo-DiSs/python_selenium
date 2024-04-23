from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

URL = 'https://parsinger.ru/selenium/5.5/4/1.html'

with webdriver.Chrome() as driver:
    driver.get(URL)

    parent_divs = driver.find_elements(By.CLASS_NAME, 'parent')

    for div in parent_divs:
        gray_textarea = div.find_element(By.XPATH, './textarea[@color="gray"]')
        number = gray_textarea.get_attribute('value')
        gray_textarea.clear()

        blue_textarea = div.find_element(By.XPATH, './textarea[@color="blue"]')
        blue_textarea.send_keys(number)

        driver.execute_script("arguments[0].scrollIntoView();", blue_textarea)

        button = div.find_element(By.TAG_NAME, 'button')

        driver.implicitly_wait(1)

        button.click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))

    check_all_btn = driver.find_element(By.ID, 'checkAll')
    check_all_btn.click()

    print(driver.find_element(By.ID, 'congrats').text)


# from selenium import webdriver
#
# url = 'https://parsinger.ru/selenium/5.5/4/1.html'
# driver = webdriver.Chrome()
# driver.get(url)
# gray = driver.find_elements('xpath', '//textarea[@color="gray"]')
# blue = driver.find_elements('xpath', '//textarea[@color="blue"]')
# buttons = driver.find_elements('xpath', '//button')
# for g, b, but in zip(gray, blue, buttons):
#     text = g.text
#     g.clear()
#     b.send_keys(text)
#     but.click()
# driver.find_element('xpath', '//button[@id="checkAll"]').click()
# print(driver.find_element('xpath','//p[@id="congrats"]').text)