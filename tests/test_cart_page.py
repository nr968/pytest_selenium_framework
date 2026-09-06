import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.parametrize(
    "product_name",
    ["Brocolli", "Carrot", "Tomato"]
)
def test_add_product_and_verify_checkout(driver: WebDriver, product_name: str):
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)

    assert "GREENKART" in products_page.get_brand_logo_text()
    products_page.search_product(product_name=product_name)
    assert product_name in products_page.get_product_name(product_name=product_name)

    products_page.add_product_to_cart(product_name=product_name)
    cart_page.click_cart()
    assert cart_page.is_product_added_to_cart(product_name=product_name)

    cart_page.click_checkout()
    products = cart_page.get_products_details()
    assert any(
        product_name in product.product_name
        for product in products
    )