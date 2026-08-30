product_page_locators = {
    'input': {
        'search_box': '//input[@class="search-keyword" and @type="search"]',
    },
    'text': {
        'brand_logo': '//div[@class="brand greenLogo"]',
        'product_card_text': '//h4[@class="product-name" and contains(text(), "{product_name}")]',
    },
    'button':{
        'search_button': '//button[@class="search-button" and @type="submit"]',
        'add_to_cart': '//button[@type="button" and contains(text(),"ADD TO CART")]',
    },
    'element': {
        'product_card': '//div[@class="product"]',
    }
}