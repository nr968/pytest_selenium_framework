from utilities.Dict2Class import dict2class

locators_dict = {
    'element': {
        'top_deals': '//a[contains(text(),"Top Deals")]',
        'discount_table': '//table[@class="table table-bordered"]',
        'discount_table_headers': '//table[@class="table table-bordered"]//thead//th',
        'discount_table_rows': '//table[@class="table table-bordered"]//tbody//tr',
    },
    'input': {
        'search_field': '//input[@id="search-field"]',
    }
}

LOCATORS = dict2class(locators_dict)