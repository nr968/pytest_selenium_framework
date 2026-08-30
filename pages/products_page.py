from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

locators = {
    'input': {
        'search_box': '//input[@class="search-keyword" and @type="search"]',
    },
    'text': {
        'brand_logo': '//div[@class="brand greenLogo"]',
        'product_card_text': '//h4[contains(text(), "{product_name}")]',
        'product_added_text': '//h4[contains(text(), {product_name})]/..//button[@type="button" and contains(text(),"ADDED")]',
        'cart_item_product_name': '//div[@class="cart-preview active"]//li[@class="cart-item"]//p[@class="product-name"]',
    },
    'button':{
        'search_button': '//button[@class="search-button" and @type="submit"]',
        'add_to_cart': '//h4[contains(text(), {product_name})]/..//button[@type="button" and contains(text(),"ADD TO CART")]',
    },
    'element': {
        'product_card': '//div[@class="product"]',
        'cart_icon': '//a[@class="cart-icon"]/img'
    }
}

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def get_brand_logo_text(self):
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators["text"]["brand_logo"])
        ))
        return self.driver.find_element(By.XPATH, locators["text"]["brand_logo"]).text

    def search_product(self, product_name: str):
        self.driver.find_element(By.XPATH, locators["input"]["search_box"]).send_keys(product_name)
        self.driver.find_element(By.XPATH, locators["button"]["search_button"]).click()

    def get_product_name_from_search_result(self, product_name: str):
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators["text"]["product_card_text"].format(product_name=product_name))
        ))
        return self.driver.find_element(By.XPATH, locators["text"]["product_card_text"].format(
            product_name=product_name)).text

    def add_product_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, locators["button"]["add_to_cart"].format(product_name=product_name)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators["text"]["product_added_text"].format(product_name=product_name))
        ))

    def is_product_added_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, locators["element"]["cart_icon"]).click()
        return product_name in self.driver.find_element(By.XPATH, locators["text"]["cart_item_product_name"]).text