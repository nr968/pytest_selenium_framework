from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.common.exceptions import StaleElementReferenceException

from utilities.Dict2Class import dict2class

class Common:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator_type: str, locator: str) -> WebElement:
        return self.driver.find_element(locator_type, locator)

    def find_elements(self, locator_type: str, locator: str) -> list[WebElement]:
        return self.driver.find_elements(locator_type, locator)

    def wait_until_element_is_visible(self, locator_type: str, locator: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located(
            (locator_type, locator)
        ))

    def wait_until_element_is_present(self, locator_type: str, locator: str):
        return self.wait.until(expected_conditions.presence_of_element_located(
            (locator_type, locator)
        ))

    def wait_until_element_is_clickable(self, locator_type: str, locator: str, timeout=10):
        return self.wait.until(expected_conditions.element_to_be_clickable(
            (locator_type, locator)
        ))

    def click_element(self, locator_type: str, locator: str) -> None:
        self.wait_until_element_is_clickable(locator_type, locator).click()

    def click_element_with_retry(self, locator_type: str, locator: str):
        retry_count = 3
        for attempt in range(retry_count):
            try:
                self.click_element(locator_type, locator)
            except StaleElementReferenceException:
                if attempt == retry_count - 1:
                    raise
                self.wait_until_element_is_present(locator_type, locator)
                self.wait_until_element_is_visible(locator_type, locator)

    def get_element_text(self, locator_type: str, locator: str) -> str:
        return self.wait_until_element_is_visible(locator_type, locator).text

    def send_keys(self, locator_type: str, locator: str, text: str) -> None:
        self.wait_until_element_is_visible(locator_type, locator).send_keys(text)

    def switch_to_new_window(self, existing_handles):
        new_window = set(self.driver.window_handles) - set(existing_handles)
        if new_window:
            self.driver.switch_to.window(new_window.pop())
        else:
            raise ValueError("New tab not opened")

    def switch_to_window(self, window_handle: str):
        self.driver.switch_to.window(window_handle)

    def close_current_window(self):
        self.driver.close()

    def read_table(self, table_xpath: str, header_xpath: str, row_xpath: str):
        self.wait_until_element_is_visible(By.XPATH, table_xpath)
        table_headers = self.find_elements(By.XPATH, header_xpath)
        headers: list[str] = []
        for header in table_headers:
            headers.append(header.text)
        table_rows = self.find_elements(By.XPATH, row_xpath)
        table_data = []
        for _ in table_rows:
            row_datas = self.find_elements(By.XPATH, f"{row_xpath}/td")
            dict_map = {}
            for header, datas in zip(headers,row_datas):
                dict_map[header] = datas.text
            table_data.append(dict2class(dict_map))
        return table_data
