import time

from selenium import webdriver
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser.get(link)
    x_element = browser.find_element_by_id('treasure').get_attribute('valuex')
    x = x_element
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn-default').click()

finally:
    time.sleep(3)
    browser.quit()
