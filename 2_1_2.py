import math
import time

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)

attribute = browser.find_element_by_css_selector("img#treasure").get_attribute("valuex")
res = calc(attribute)
browser.find_element_by_css_selector("input#answer").send_keys(res)
browser.find_element_by_css_selector("input#robotCheckbox").click()
browser.find_element_by_css_selector("input#robotsRule").click()
browser.find_element_by_css_selector("button[type=submit]").click()
time.sleep(1)
pass