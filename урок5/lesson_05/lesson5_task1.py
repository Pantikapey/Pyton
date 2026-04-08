import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_class_name():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/classattr")
    element = driver.find_element(By.CLASS_NAME, "btn class1 btn-privary btn-test")

    assert element is not None
    assert element.tag_name == "input"

    driver.quit()
