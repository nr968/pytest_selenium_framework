from selenium import webdriver

from utilities import config_reader

import pytest


@pytest.fixture
def driver():
    config = config_reader.get_config()

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config["base_url"])
    yield driver
    driver.quit()