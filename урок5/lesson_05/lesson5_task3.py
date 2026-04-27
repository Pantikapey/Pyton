from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(10)
driver.find_element(By.CSS_SELECTOR,".example > input:nth-child(2)").clear()
sleep(5)
driver.quit()                 


    
