from pages.common import Common

from locators.dynamic_page import LOCATORS

class DynamicPage(Common):

    def get_fixed_table_details(self):
        table = LOCATORS.element.dynamic_table
        table_header = LOCATORS.element.dynamic_table_headers
        table_rows = LOCATORS.element.dynamic_table_rows
        return self.read_table(table_xpath=table, header_xpath=table_header, row_xpath=table_rows)
