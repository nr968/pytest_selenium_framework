from pages.products_page import ProductsPage


def test_product_page_loaded(driver):
    assert driver.title == "GreenKart - veg and fruits kart"

def test_search_product_and_verify_result(driver):
    products_page = ProductsPage(driver)
    product_name = "Brocolli"

    assert "GREENKART" in products_page.get_brand_logo_text()
    products_page.search_product(product_name=product_name)
    assert product_name in products_page.get_product_name(product_name=product_name)
    products_page.add_product_to_cart(product_name=product_name)
    products_page.click_cart()
    assert products_page.is_product_added_to_cart(product_name=product_name)