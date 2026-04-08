# ввести в поле 12345
# очистить это поле метод clear()
# ввести в поле 54321
# закрыть браузер (метод quit())


import os
import subprocess
import sys

import pytest
from selenium import webdriver

def test_css_selector(driver):
    driver = webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/inputs")
    element = driver.find_element(By.CSS_SELECTOR, ".example > input:nth-child(2)")

    assert element is not None
    assert element.get_attribute("value") == "Jane"

    driver.quit()

    