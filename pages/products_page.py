from selenium.webdriver.common.by import By

from pages.common import Common

from locators.products_page import LOCATORS

class ProductsPage(Common):

    def __init__(self, driver):
        super().__init__(driver)

    def get_brand_logo_text(self):
        return self.get_element_text(By.XPATH, LOCATORS.text.brand_logo)

    def search_product(self, product_name: str):
        self.send_keys(By.XPATH, LOCATORS.input.search_box, product_name)
        self.click_element(By.XPATH, LOCATORS.button.search_button)

    def get_product_name(self, product_name: str):
        return self.get_element_text(By.XPATH, LOCATORS.text.product_card_text.format(product_name=product_name))

    def add_product_to_cart(self, product_name):
        self.click_element(By.XPATH, LOCATORS.button.add_to_cart.format(product_name=product_name))
        self.wait_until_element_is_visible(By.XPATH, LOCATORS.text.product_added_text.format(product_name=product_name))