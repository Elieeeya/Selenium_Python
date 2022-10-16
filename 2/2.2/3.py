import time

from selenium import webdriver

from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)


def sum(x1, x2):
    return str(int(x1) + int(x2))


x = browser.find_element_by_id('num1').text
y = browser.find_element_by_id('num2').text
z = sum(x, y)
select = Select(browser.find_element_by_class_name('custom-select'))
select.select_by_value(z)
browser.find_element_by_class_name('btn-default').click()
time.sleep(5)
browser.quit()
