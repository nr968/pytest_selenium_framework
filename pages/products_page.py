from selenium.webdriver.common.by import By

from pages.common import Common

from locators.products_page import locators

class ProductPage(Common):

    def __init__(self, driver):
        super().__init__(driver)

    def get_brand_logo_text(self):
        return self.wait_until_element_is_visible(By.XPATH, locators["text"]["brand_logo"]).text

    def search_product(self, product_name: str):
        self.find_element(By.XPATH, locators["input"]["search_box"]).send_keys(product_name)
        self.find_element(By.XPATH, locators["button"]["search_button"]).click()

    def get_product_name(self, product_name: str):
        return self.wait_until_element_is_visible(
            By.XPATH, locators["text"]["product_card_text"].format(product_name=product_name)).text

    def add_product_to_cart(self, product_name):
        self.find_element(By.XPATH, locators["button"]["add_to_cart"].format(product_name=product_name)).click()
        self.wait_until_element_is_visible(By.XPATH, locators["text"]["product_added_text"].format(product_name=product_name))

    def click_cart(self):
        locator_type = By.XPATH
        locator = locators["element"]["cart_icon"]
        self.wait_until_element_is_visible(locator_type, locator).click()

    def is_product_added_to_cart(self, product_name):
        return product_name in self.find_element(By.XPATH, locators["text"]["cart_item_product_name"]).text