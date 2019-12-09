import os 

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

browser.find_element_by_xpath("//input[@name='firstname']").send_keys('Маша')
browser.find_element_by_xpath("//input[@name='lastname']").send_keys('Скворцова')
browser.find_element_by_xpath("//input[@name='email']").send_keys('test@test.ru')
browser.find_element_by_xpath("//input[@name='file']").send_keys(file_path)
browser.find_element_by_xpath("//button[@type='submit']").click()


pass