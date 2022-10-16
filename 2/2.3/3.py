import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

browser.find_element_by_class_name('btn-primary').click()

alert = browser.switch_to_alert()
alert.accept()

x_element = browser.find_element_by_id('input_value').text
x = x_element


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_class_name('btn-primary').click()

time.sleep(3)
browser.quit()