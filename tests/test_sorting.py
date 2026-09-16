import allure
import pytest

from pages.login_page import LoginPage
from utils.base_class import BaseClass


@pytest.mark.usefixtures("init_browser")
@allure.feature("Sorting Inventory")
class TestSorting(BaseClass):

    logger = BaseClass.get_logger()
    data = BaseClass.get_data_from_json("data.json")

    # Login Credentials
    username = data["login_credentials"]["username"]
    password = data["login_credentials"]["password"]

    def login_to_inventory(self):

        login_page = LoginPage(self.driver)

        self.logger.info(
            f"Logging in with username '{self.username}'."
        )

        inventory_page = login_page.login(
            self.username,
            self.password
        )

        self.logger.info(
            "Verifying the Inventory page is loaded."
        )

        assert "inventory.html" in inventory_page.get_current_url(), (
            "Inventory page was not loaded."
        )

        return inventory_page

    @allure.title("TC-006: Sort Products by Name (A-Z)")
    @allure.story("Sort Products by Name")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "Verify that products are displayed in ascending alphabetical "
        "order when Name (A-Z) sorting is selected."
    )
    def test_a_to_z_name_sort(self):

        self.logger.info(
            "Starting TC-006: Verify products are sorted by Name (A-Z)."
        )

        inventory_page = self.login_to_inventory()

        self.logger.info(
            "Sorting products by Name (A-Z)."
        )

        inventory_page.sort_items(
            inventory_page.sort_by_az
        )

        item_names = inventory_page.get_items_name_list()


        self.logger.info(
            "Verifying products are displayed in ascending "
            "alphabetical order."
        )

        assert item_names == sorted(item_names), (
            "Products are not sorted alphabetically in ascending order."
        )

    @allure.title("TC-007: Sort Products by Name (Z-A)")
    @allure.story("Sort Products by Name")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "Verify that products are displayed in descending alphabetical "
        "order when Name (Z-A) sorting is selected."
    )
    def test_z_to_a_name_sort(self):

        self.logger.info(
            "Starting TC-007: Verify products are sorted by Name (Z-A)."
        )

        inventory_page = self.login_to_inventory()

        self.logger.info(
            "Sorting products by Name (Z-A)."
        )

        inventory_page.sort_items(
            inventory_page.sort_by_za
        )

        item_names = inventory_page.get_items_name_list()

        self.logger.info(
            "Verifying products are displayed in descending "
            "alphabetical order."
        )

        assert item_names == sorted(item_names, reverse=True), (
            "Products are not sorted alphabetically in descending order."
        )

    @allure.title("TC-008: Sort Products by Price (Low to High)")
    @allure.story("Sort Products by Price")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "Verify that products are displayed from the lowest price "
        "to the highest price when Price (Low to High) sorting "
        "is selected."
    )
    def test_low_to_high_sort_price(self):

        self.logger.info(
            "Starting TC-008: Verify products are sorted by "
            "Price (Low to High)."
        )

        inventory_page = self.login_to_inventory()

        self.logger.info(
            "Sorting products by Price (Low to High)."
        )

        inventory_page.sort_items(
            inventory_page.sort_by_low_high
        )

        item_prices = inventory_page.get_items_price_list()

        self.logger.info(
            "Verifying products are displayed from lowest "
            "price to highest price."
        )

        assert item_prices == sorted(item_prices), (
            "Products are not sorted by price from low to high."
        )

    @allure.title("TC-009: Sort Products by Price (High to Low)")
    @allure.story("Sort Products by Price")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "Verify that products are displayed from the highest price "
        "to the lowest price when Price (High to Low) sorting "
        "is selected."
    )
    def test_high_to_low_sort_price(self):

        self.logger.info(
            "Starting TC-009: Verify products are sorted by "
            "Price (High to Low)."
        )

        inventory_page = self.login_to_inventory()

        self.logger.info(
            "Sorting products by Price (High to Low)."
        )

        inventory_page.sort_items(
            inventory_page.sort_by_high_low
        )

        item_prices = inventory_page.get_items_price_list()

        self.logger.info(
            "Verifying products are displayed from highest "
            "price to lowest price."
        )

        assert item_prices == sorted(item_prices, reverse=True), (
            "Products are not sorted by price from high to low."
        )