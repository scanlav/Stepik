import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(_x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'


try:
    browser.get(link)
    # time.sleep(2)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input_x = browser.find_element(By.ID, 'answer')
    input_x.send_keys(y)
    chekbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", chekbox)
    chekbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    submit = browser.find_element(
        By.CSS_SELECTOR, 'button.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()


finally:
    time.sleep(20)
    browser.quit()
