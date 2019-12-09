import math

from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_xpath("//button[@type='submit']").click()

confirm = browser.switch_to.alert
confirm.accept()

number = browser.find_element_by_xpath("//span[@id='input_value']").text
res = calc(number)

browser.find_element_by_xpath("//input[@id='answer']").send_keys(res)
browser.find_element_by_xpath("//button[@type='submit']").click()

pass