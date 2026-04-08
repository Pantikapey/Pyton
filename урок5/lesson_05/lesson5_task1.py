
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")
    element = driver.find_element(By.CLASS_NAME, "information")

    assert element is not None
    assert element.tag_name == "input"

    driver.quit()

