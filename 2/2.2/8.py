import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

browser.find_element_by_name('firstname').send_keys('Ivan')
browser.find_element_by_name('lastname').send_keys('Ivanov')
browser.find_element_by_name('email').send_keys('Inav.Ivanov@mail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element_by_id('file').send_keys(file_path)

browser.find_element_by_class_name('btn-primary').click()

time.sleep(3)
browser.quit()