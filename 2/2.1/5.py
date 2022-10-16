import time

from selenium import webdriver
import math

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/math.html'





try:
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_class_name('form-check-label').click()
    browser.find_element_by_xpath("//label[text()='Robots rule']").click()
    time.sleep(3)
    browser.find_element_by_class_name('btn-default').click()

finally:
    time.sleep(10)
    browser.quit()
