from locators.cart_page import LOCATORS

from pages.common import Common

from selenium.webdriver.common.by import By

from utilities.Dict2Class import dict2class

class CartPage(Common):

    def click_cart(self):
        self.click_element(By.XPATH, LOCATORS.element.cart_icon)

    def is_product_added_to_cart(self, product_name):
        return product_name in self.get_element_text(By.XPATH, LOCATORS.text.cart_item_product_name)

    def click_checkout(self):
        self.click_element(By.XPATH, LOCATORS.button.checkout_button)
        self.wait_until_element_is_visible(By.XPATH, LOCATORS.element.checkout_table)

    def get_products_details(self) -> list[object]:
        checkout_product_table_headers = self.find_elements(By.XPATH, LOCATORS.element.checkout_table_headers)
        headers = []
        for header in checkout_product_table_headers[1:]:
            headers.append(header.text)

        products = []
        checkout_product_table_rows = self.find_elements(By.XPATH, LOCATORS.element.checkout_table_rows)
        for row in checkout_product_table_rows:
            product_details = self.find_elements(By.XPATH, f"{LOCATORS.element.checkout_table_rows}/td")[1:]
            if len(headers) == len(product_details):
                map_dict = {}
                for header, product_detail in zip(headers, product_details):
                    map_dict[header] = product_detail.text
                print(map_dict)
                products.append(dict2class(map_dict))
            else:
                raise ValueError(f'Header and row length does not match')
        return products