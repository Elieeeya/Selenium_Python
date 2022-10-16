import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'
browser.get(link)
x_element = browser.find_element_by_id('input_value').text
x = x_element


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)
browser.find_element_by_id('answer').send_keys(y)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_class_name('btn-primary').click()



time.sleep(3)
browser.quit()
