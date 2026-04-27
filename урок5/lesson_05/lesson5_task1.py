from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr.")
sleep(10)
driver.find_element(By.CSS_SELECTOR, "body > section > div > button.btn.class2.btn-primary.btn-test").click()

driver.quit()
