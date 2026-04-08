import os
import subprocess
import sys

import pytest
from selenium import webdriver


def test_basic_options():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    driver.quit()

