from selenium import webdriver

from utilities import config_reader

import pytest

config = config_reader.get_config()

@pytest.fixture
def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config["base_url"])
    yield driver
    driver.quit()