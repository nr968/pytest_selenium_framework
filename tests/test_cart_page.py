import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.parametrize(
    "product_name",
    ["Brocolli", "Carrot", "Tomato"]
)
def test_verify_product_is_added_to_cart(driver: WebDriver, product_name: str):
    products_page = ProductsPage(driver)
    cart = CartPage(driver)

    assert "GREENKART" in products_page.get_brand_logo_text()
    products_page.search_product(product_name=product_name)
    assert product_name in products_page.get_product_name(product_name=product_name)

    products_page.add_product_to_cart(product_name=product_name)
    cart.click_cart()
    assert cart.is_product_added_to_cart(product_name=product_name)

    cart.click_checkout()
    products = cart.get_products_details()
    for product in products:
        assert product_name in product.product_name