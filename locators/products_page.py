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