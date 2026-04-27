from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
sleep(10)
driver.find_element(By.CSS_SELECTOR,".fa").click()
driver.quit()

