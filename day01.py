from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
#driver=webdriver.Firefox
print("start")
driver.get("D:\\注册.html")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")

sleep(4)
driver.quit()
