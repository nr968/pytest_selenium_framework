from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.products_page import product_page_locators


def test_product_page_loaded(driver):
    assert driver.title == "GreenKart - veg and fruits kart"

def test_product_search_and_result(driver):
    wait = WebDriverWait(driver, 5)
    product_name = "Brocolli"

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, product_page_locators["text"]["brand_logo"])
    ))
    driver.find_element(By.XPATH, product_page_locators["input"]["search_box"]).send_keys(product_name)
    driver.find_element(By.XPATH, product_page_locators["button"]["search_button"]).click()
    assert len(driver.find_elements(By.XPATH, product_page_locators["element"]["product_card"])) == 1

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, product_page_locators["text"]["product_card_text"].format(product_name=product_name))
    ))
    assert product_name in driver.find_element(By.XPATH, product_page_locators["text"]["product_card_text"].format(product_name=product_name)).text