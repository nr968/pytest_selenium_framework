def test_product_page_loaded(create_driver):
    assert create_driver.title == "GreenKart - veg and fruits kart"