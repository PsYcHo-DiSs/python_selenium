from selenium import webdriver

URL = 'https://parsinger.ru/methods/3/index.html'

with webdriver.Chrome() as webdriver:
    webdriver.get(URL)
    cookies = webdriver.get_cookies()
    target_total = 0
    for dct in cookies:
        target = int(dct['name'].split('_')[2])
        target_total += int(dct['value'])

print(target_total)
