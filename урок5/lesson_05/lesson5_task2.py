from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid.")
for i in range(3)

blue_button = driver.find_element(By.CSS_SELECTOR, 'dir.auto').click()

driver.quit()
