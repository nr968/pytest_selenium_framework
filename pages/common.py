from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

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

    def click_element(self, locator_type: str, locator: str) -> None:
        self.wait_until_element_is_visible(locator_type, locator).click()

    def get_element_text(self, locator_type: str, locator: str) -> str:
        return self.wait_until_element_is_visible(locator_type, locator).text

    def send_keys(self, locator_type: str, locator: str, text: str) -> None:
        self.wait_until_element_is_visible(locator_type, locator).send_keys(text)

    def switch_to_new_tab(self):
        return self.driver.window_handles[-1]

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
