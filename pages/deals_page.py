from selenium.webdriver.chrome.webdriver import WebDriver

from conftest import driver
from pages.common import Common

from locators.deals_page import LOCATORS

from selenium.webdriver.common.by import By

class DealsPage(Common):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_deals_link(self):
        current_window = self.driver.current_window_handle
        self.click_element(By.XPATH, LOCATORS.element.top_deals)
        windows = self.driver.window_handles
        for window in windows:
            if window != current_window:
                self.driver.switch_to.window(window)
                break

    def search_discount_product(self, product_name):
        # self.click_element(By.XPATH, LOCATORS.input.search_field)
        self.send_keys(By.XPATH, LOCATORS.input.search_field, product_name)

    def get_discount_details(self):
        table_xpath = LOCATORS.element.discount_table
        table_headers_xpath = LOCATORS.element.discount_table_headers
        table_rows_xpath = LOCATORS.element.discount_table_rows
        return self.read_table(table_xpath, table_headers_xpath, table_rows_xpath)