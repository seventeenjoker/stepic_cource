import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

num1 = browser.find_element_by_css_selector("span#num1").text
num2 = browser.find_element_by_css_selector("span#num2").text
res = str(int(num1) + int(num2))
select = Select(browser.find_element_by_css_selector("select#dropdown"))
select.select_by_value(res)

browser.find_element_by_css_selector("button[type=submit]").click()
time.sleep(5)
pass