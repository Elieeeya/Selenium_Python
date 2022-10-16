from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

link_one = 'http://suninjuly.github.io/registration1.html'
link_two = 'http://suninjuly.github.io/registration2.html'

letters = string.ascii_lowercase
random_letters = (''.join(random.choice(letters) for i in range(10)))


def test_link_one():
    try:
        browser = webdriver.Chrome()
        browser.get(link_one)

        required_elements = browser.find_elements_by_css_selector('input[required]')
        for element in required_elements:
            element.send_keys(random_letters)

        button = browser.find_element_by_class_name('btn-default')
        button.click()


    finally:
        # успеваем скопировать код за 5 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла


def test_link_two():
    try:
        browser = webdriver.Chrome()
        browser.get(link_two)

        required_elements = browser.find_elements_by_css_selector('input[required]')
        for element in required_elements:
            element.send_keys(random_letters)

        button = browser.find_element_by_class_name('btn-default')
        button.click()


    finally:
        # успеваем скопировать код за 5 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла
