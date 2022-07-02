import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'


def calc(_x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(10)
    browser.quit()
