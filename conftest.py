from email.policy import default

from robot.variables import store
from selenium import webdriver

from utilities import config_reader

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="v2",
        help="URL version"
    )
    parser.addoption(
        "--api",
        action="store",
        default="https://api.eventhub.rahulshettyacademy.com/api",
        help="base url for api"
    )

@pytest.fixture()
def base_url(request):
    url_version = request.config.getoption("--url")
    config = config_reader.get_config()
    urls = config["urls"] if isinstance(config, dict) else config[0]["urls"]

    if url_version not in urls:
        valid_versions = ", ".join(urls.keys())
        raise ValueError(f"Invalid URL version: {url_version}.\nValid URL versions: {valid_versions}")

    return urls[url_version]

@pytest.fixture
def api_url(request):
    return request.config.getoption("--api")

@pytest.fixture
def driver(base_url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)

    yield driver

    driver.quit()