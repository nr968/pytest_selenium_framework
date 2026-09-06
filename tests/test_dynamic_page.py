import pytest

from pages.dynamic_page import DynamicPage

from utilities.test_data_reader import load_test_data

dynamic_table_details = load_test_data("dynamic_table.json")

@pytest.mark.parametrize(
    "dynamic_table",
    dynamic_table_details
)
def test_name_from_city_and_position(driver, dynamic_table):
    dynamic_page = DynamicPage(driver)
    table_details = dynamic_page.get_fixed_table_details()
    matching_row = None
    for row in table_details:
        if row.position == dynamic_table["position"] and row.city == dynamic_table["city"]:
            matching_row = row
            break
    assert matching_row is not None, [f"No matching row found for position: {dynamic_table['position']}"
                                      f" and city: {dynamic_table['city']}"]
    assert matching_row.name == dynamic_table["name"]
