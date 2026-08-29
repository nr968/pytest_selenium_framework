from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    yield driver
    driver.quit()