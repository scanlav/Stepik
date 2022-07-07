# я так и не понял, как спихнуть этот импорт в conftest, что бы тест не ругался
from selenium.webdriver.common.by import By


def test_items(browser):
    assert browser.find_element(
        By.CSS_SELECTOR, 'button.btn-add-to-basket'), 'Could not find button'
