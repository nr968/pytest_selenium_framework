from locators.cart_page import LOCATORS

from pages.common import Common

from selenium.webdriver.common.by import By

class CartPage(Common):

    def click_cart(self):
        self.click_element(By.XPATH, LOCATORS.element.cart_icon)

    def is_product_added_to_cart(self, product_name):
        return product_name in self.get_element_text(By.XPATH, LOCATORS.text.cart_item_product_name)

    def click_checkout(self):
        self.click_element(By.XPATH, LOCATORS.button.checkout_button)
        self.wait_until_element_is_visible(By.XPATH, LOCATORS.element.checkout_table)

    def get_products_details(self) -> list[object]:
        checkout_table = LOCATORS.element.checkout_table
        checkout_product_table_headers = LOCATORS.element.checkout_table_headers
        checkout_product_table_rows = LOCATORS.element.checkout_table_rows
        return self.read_table(checkout_table, checkout_product_table_headers, checkout_product_table_rows)