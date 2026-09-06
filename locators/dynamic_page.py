from utilities.Dict2Class import dict2class

locators_dict = {
    'element': {
        'dynamic_table': '//div[@class="tableFixHead"]/table[@id="product"]',
        'dynamic_table_headers': '//div[@class="tableFixHead"]/table[@id="product"]//thead//th',
        'dynamic_table_rows': '//div[@class="tableFixHead"]/table[@id="product"]//tbody/tr'
    }
}

LOCATORS = dict2class(locators_dict)