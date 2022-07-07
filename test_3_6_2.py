# pylint: disable=syntax-error
import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def browser():
    print('\n start test')
    browser = webdriver.Chrome()
    yield browser
    print('\n finish test')
    browser.quit()


@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
])
class TestStepik():
    def test_answer(self, browser, link):
        link = f'{link}'
        browser.get(link)
        time.sleep(15)
        answer = math.log(int(time.time()))
        browser.find_element(
            By.CLASS_NAME, 'ember-text-area').send_keys(answer)
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        time.sleep(7)
        correct_text = browser.find_element(
            By.CLASS_NAME, 'smart-hints__hint').text
        assert 'Correct!' == correct_text, correct_text
