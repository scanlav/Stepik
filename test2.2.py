import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects2.html'


try:

    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    sum_num = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(sum_num))

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:

    time.sleep(10)
    browser.quit()
