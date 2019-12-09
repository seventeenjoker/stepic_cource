import math
import time

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)
x = browser.find_element_by_css_selector('span#input_value').text
result = calc(x)
input_res = browser.find_element_by_css_selector("input#answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_res)
input_res.send_keys(result)
browser.find_element_by_css_selector("input#robotCheckbox").click()
browser.find_element_by_css_selector("input#robotsRule").click()
button_submit = browser.find_element_by_css_selector("button[type=submit]")
browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
button_submit.click()
pass
