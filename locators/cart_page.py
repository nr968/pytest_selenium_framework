from utilities.Dict2Class import dict2class

locators_dict = {
    'button': {
        'checkout_button': '//button[contains(text(),"PROCEED TO CHECKOUT")]'
    },
    'text': {
        'cart_item_product_name': '//div[contains(@class,"cart-preview")]//li[@class="cart-item"]//p[@class="product-name"]',
    },
    'element': {
        'cart_icon': '//a[@class="cart-icon"]/img',
        'checkout_table': '//table[@id="productCartTables"]',
        'checkout_table_headers': '//table[@id="productCartTables"]/thead//tr/td',
        'checkout_table_rows': '//table[@id="productCartTables"]/tbody//tr',
    }
}

LOCATORS = dict2class(locators_dict)