import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_site1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(
            By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys('Ivan')
        input2 = browser.find_element(
            By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys('Petrov')
        input3 = browser.find_element(
            By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys('ivan@g.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text_elt.text, welcome_text, "Error!")
        browser.quit()

    def test_site2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(
            By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys('Ivan')
        input2 = browser.find_element(
            By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        input2.send_keys('Petrov')
        input3 = browser.find_element(
            By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        input3.send_keys('ivan@g.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text_elt.text, welcome_text, "Error!")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
