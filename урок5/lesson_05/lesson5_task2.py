from selenium import webdriver
from selenium.webdriver.common.by import By


def test_id(driver):
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/dynamicid")
    element = driver.find_element(By.ID, "05a30e8e-aea1-e10e-4f51-e85db3872271")

    assert element is not None
    assert element.get_attribute("value") == "Doe"

    driver.quit()
