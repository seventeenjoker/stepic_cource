import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_id('book')
button.click()

# WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID, "input_value"))

t_1 = browser.find_element_by_xpath("//*[@id='input_value']").text
res = calc(int(t_1))
browser.find_element_by_xpath("//*[@id='answer']").send_keys(res)
browser.find_element_by_xpath("//*[@id='solve']").click()

pass