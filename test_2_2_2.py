# импортируем нужные модули, иначе ничего не сработает
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализируем браузер, в котором будем тестировать
browser = webdriver.Chrome()
# ссылка для тестирования
link = 'http://suninjuly.github.io/file_input.html'

# создаем условия, при которых в случае ошибки, процесс все равно завершится
try:
    # открываем подопытную ссылку в окне браузера
    browser.get(link)

    # заполняем форму
    input1 = browser.find_element(By.NAME, 'firstname').send_keys('Ivan')
    input2 = browser.find_element(By.NAME, 'lastname').send_keys('Petrov')
    input3 = browser.find_element(By.NAME, 'email').send_keys('ivan@mail.com')

    # указываем путь до файла и имя файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    # определяем поле для загрузки файла и передаем путь
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)

    # жмем подтверждение, работа закончена :)
    submit = browser.find_element(
        By.CSS_SELECTOR, 'button.btn-primary').click()

finally:
    # если не успеваем скопировать код, увеличить счетчик
    time.sleep(10)

    # обязательно завершаем процесс тестирования, даже если ничего не получилось =_=
    browser.quit()

# Пустая строка. Нужна, что бы при запуске файла через терминал, обрабатывалась последняя строка. Иначе игнор :(
