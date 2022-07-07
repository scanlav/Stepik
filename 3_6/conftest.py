import pytest
import time
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru')


@pytest.fixture(scope="function")
def browser(request):
    link = f"http://selenium1py.pythonanywhere.com/{request.config.getoption('language')}/catalogue/coders-at-work_207/"
    print(
        f"\nstart browser for test.. lang = {request.config.getoption('language')}")
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(30)
    yield browser
    print("\nquit browser..")
    browser.quit()
