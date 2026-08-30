from pages.products_page import ProductPage


def test_product_page_loaded(driver):
    assert driver.title == "GreenKart - veg and fruits kart"

def test_search_product_and_verify_result(driver):
    products_page = ProductPage(driver)
    product_name = "Brocolli"

    products_page.verify_page_loaded()
    products_page.search_product(product_name=product_name)
    products_page.verify_product_in_search_result(product_name=product_name)
    products_page.add_product_to_cart(product_name=product_name)
    products_page.verify_product_added_to_cart(product_name=product_name)