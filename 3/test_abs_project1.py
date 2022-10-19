from selenium import webdriver
import time
import string
import random
import unittest

from selenium.webdriver.common.by import By

link_one = 'http://suninjuly.github.io/registration1.html'
link_two = 'http://suninjuly.github.io/registration2.html'

letters = string.ascii_lowercase
random_letters = (''.join(random.choice(letters) for i in range(10)))

browser = webdriver.Chrome()
elements = []


class TestAbs(unittest.TestCase):
    def test_link_one(self):
        try:
            browser.get(link_one)
            elements.append(browser.find_element(By.CSS_SELECTOR, "div.first_block input.first"))
            # Если убрать то тест успешный
            elements.append(browser.find_element(By.CSS_SELECTOR, "div.first_block input.second"))

            elements.append(browser.find_element(By.CSS_SELECTOR, "div.first_block input.third"))
            for element in elements:
                element.send_keys(random_letters)

            button = browser.find_element(By.CLASS_NAME, 'btn-default')
            button.click()
        finally:
            self.assertEqual('Congratulations! You have successfully registered!', "Congratulations! You have successfully registered!")
            browser.quit()

    def test_link_two(self):
        try:
            browser.get(link_two)
            elements.append(browser.find_element(By.CSS_SELECTOR, "div.first_block input.first"))

            # Если убрать то тест успешный
            # elements.append(browser.find_element(By.CSS_SELECTOR, "div.first_block input.second"))

            elements.append(browser.find_element(By.CSS_SELECTOR, "div.first_block input.third"))
            for element in elements:
                element.send_keys(random_letters)

            button = browser.find_element(By.CLASS_NAME, 'btn-default')
            button.click()
        finally:
            # успеваем скопировать код за 5 секунд
            self.assertEqual('Congratulations! You have successfully registered!', "Congratulations! You have successfully registered!")
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()
