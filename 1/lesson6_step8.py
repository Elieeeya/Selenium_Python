from selenium import webdriver
import time
import string
import random

link_one = 'http://suninjuly.github.io/registration1.html'
link_two = 'http://suninjuly.github.io/registration2.html'

letters = string.ascii_lowercase
random_letters = (''.join(random.choice(letters) for i in range(10)))

browser = webdriver.Chrome()
elements = []


def test_link_one():
    try:
        browser.get(link_one)
        elements.append(browser.find_element_by_css_selector(
            "div.first_block input.first"))
        elements.append(browser.find_element_by_css_selector(
            "div.first_block input.second"))
        elements.append(browser.find_element_by_css_selector(
            "div.first_block input.third"))
        for element in elements:
            element.send_keys(random_letters)
        button = browser.find_element_by_class_name('btn-default')
        time.sleep(3)
        button.click()
    finally:
        # успеваем скопировать код за 5 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_link_two():
    try:
        browser.get(link_two)
        elements.append(browser.find_element_by_css_selector(
            "div.first_block input.first"))
        # Если убрать то тест успешный
        elements.append(browser.find_element_by_css_selector(
            "div.first_block input.second"))
        elements.append(browser.find_element_by_css_selector(
            "div.first_block input.third"))
        for element in elements:
            element.send_keys(random_letters)
        button = browser.find_element_by_class_name('btn-default')
        button.click()
    finally:
        # успеваем скопировать код за 5 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
