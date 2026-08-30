from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Common:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def find_element(self, locator_type: str, locator: str) -> WebElement:
        return self.driver.find_element(locator_type, locator)

    def wait_until_element_is_visible(self, locator_type: str, locator: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located(
            (locator_type, locator)
        ))

    def click_element(self, locator_type: str, locator: str):
        self.wait_until_element_is_visible(locator_type, locator).click()

    def get_element_text(self, locator_type: str, locator: str):
        return self.wait_until_element_is_visible(locator_type, locator).text

    def send_keys(self, locator_type: str, locator: str, text: str):
        self.wait_until_element_is_visible(locator_type, locator).send_keys(text)