import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.deals_page import DealsPage

@pytest.mark.parametrize(
    "product_name",
    ["Wheat", "Orange", "Banana"]
)
def test_search_product_and_verify_discount_price(driver: WebDriver, product_name):
    deals_page = DealsPage(driver)
    deals_page.click_deals_link()
    deals_page.search_discount_product(product_name)
    discount_details = deals_page.get_discount_details()
    for discount_detail in discount_details:
        print(discount_detail.veg_fruit_name)
        if discount_detail.veg_fruit_name.lower() == product_name.lower():
            assert discount_detail.discount_price < discount_detail.price
            break