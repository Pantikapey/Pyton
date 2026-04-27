from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(" http://uitestingplayground.com/dynamicid.")
driver.find_element(By.LINK_TEXT, "Button with Dynamic ID").click()

driver.quit()
