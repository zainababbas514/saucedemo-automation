import allure
import pytest

from pages.login_page import LoginPage
from utils.base_class import BaseClass


@pytest.mark.usefixtures("init_browser")
@allure.feature("Inventory and Cart Functionality")
class TestInventoryCart(BaseClass):
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

    @allure.story("Product Catalog Display")
    @allure.title("TC-001: Verify Product List, Images, Names, and Prices")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description(
        "Ensure the product list loads correctly, with each product "
        "showing image, name, and price."
    )
    def test_inventory_items(self):

        self.logger.info(
            "Starting TC-001: Verify that all products are displayed "
            "correctly on the Inventory page."
        )

        inventory_page = self.login_to_inventory()
        inventory_items = inventory_page.get_inventory_list()

        assert len(inventory_items) > 0, (
            "No inventory items are displayed."
        )

        # Get inventory item details
        self.logger.info(
            "Verifying each product has an image, name, and price."
        )

        items = inventory_page.get_inventory_items_details()

        for item in items:
            # Image
            assert item["image_displayed"], (
                f"Image is not displayed for "
                f"'{item['item_name']}'."
            )

            assert item["item_image"], f"Image src is empty for {item['item_name']}"

            # Name
            assert item["item_name"], "Product name is empty."
            assert item["name_displayed"], "Product name is not displayed"

            # Price
            assert item["price_displayed"], (
                f"Price is not displayed for "
                f"'{item['item_name']}'."
            )

            price_value = float(
                item["item_price"].replace("$", "").strip()
            )

            assert price_value > 0, (
                f"Price should be greater than 0 for "
                f"'{item['item_name']}', "
                f"found: {price_value}"
            )

    @pytest.mark.parametrize(
        "item_count",
        data["TC-002"]
    )

    @allure.story("Cart Management")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Verify that a single and multiple products can be "
        "successfully added to the cart."
    )
    def test_add_items_to_cart(self, item_count):

        allure.dynamic.title(
            f"TC-002: Add {item_count['add_to_cart_item_count']} item(s) to Cart"
        )

        self.logger.info(
            "Starting TC-002: Verify that a single and multiple "
            "products can be successfully added to the cart."
        )

        inventory_page = self.login_to_inventory()
        add_item_to_cart_count = item_count["add_to_cart_item_count"]

        # Add items to cart
        self.logger.info(
            f"Adding {add_item_to_cart_count} items to the cart."
        )

        selected_items = inventory_page.add_items_to_cart(
            add_item_to_cart_count
        )

        # Verify cart badge
        self.logger.info(
            "Verifying cart badge is showing correct item count."
        )

        badge_count = inventory_page.get_cart_badge_count()

        assert badge_count == add_item_to_cart_count, (
            f"Expected cart badge count "
            f"{add_item_to_cart_count}, "
            f"but got {badge_count}"
        )

        # Verify Add to cart buttons changed to Remove
        self.logger.info(
            "Verifying added items are showing Remove button."
        )

        items_status = inventory_page.get_items_cart_button_status()

        added_item_names = [
            item["item_name"]
            for item in selected_items
        ]

        for item in items_status:

            if item["item_name"] in added_item_names:

                assert item["button_text"] == "Remove", (
                    f"'{item['item_name']}' does not show "
                    f"Remove button."
                )

            else:

                assert item["button_text"] == "Add to cart", (
                    f"'{item['item_name']}' shows Remove button "
                    f"while it was not added."
                )

    @allure.story("Cart Management")
    @allure.title("TC-003: Verify Added Items Persist and Match on Cart Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Verify that products added from the Inventory page "
        "are displayed correctly on the Cart page."
    )
    def test_cart_shows_added_items(self):

        self.logger.info(
            "Starting TC-003: Verify cart page displays "
            "added products correctly."
        )

        inventory_page = self.login_to_inventory()

        add_item_to_cart_count = (
            self.data["TC-003"]["add_to_cart_item_count"]
        )

        # Add items to cart
        self.logger.info(
            f"Adding {add_item_to_cart_count} items to the cart."
        )

        selected_items = inventory_page.add_items_to_cart(
            add_item_to_cart_count
        )

        # Open cart
        self.logger.info("Opening the cart page.")

        cart_page = inventory_page.open_cart_page()

        cart_items = cart_page.get_cart_items_details()

        # Verify cart items
        self.logger.info(
            "Verifying selected items and cart items are the same."
        )

        assert selected_items == cart_items, (
            "Selected items and cart items do not match."
        )

    @allure.story("Cart Management")
    @allure.title("TC-004: Verify Product Removal from Cart Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Verify that a product can be removed from the Cart page "
        "and the remaining cart contents are updated correctly."
    )
    def test_remove_item_from_cart(self):

        self.logger.info(
            "Starting TC-004: Verify that a user can remove "
            "a product from the cart page successfully."
        )

        inventory_page = self.login_to_inventory()

        # Test Data
        add_item_to_cart_count = (
            self.data["TC-004"]["add_to_cart_item_count"]
        )

        remove_item_count = (
            self.data["TC-004"]["remove_from_cart_item_count"]
        )

        # Add Items to Cart
        self.logger.info(
            f"Adding {add_item_to_cart_count} item(s) to the cart."
        )

        selected_items = inventory_page.add_items_to_cart(
            add_item_to_cart_count
        )

        # Open Cart
        self.logger.info(
            "Opening the cart page."
        )

        cart_page = inventory_page.open_cart_page()

        cart_items = cart_page.get_cart_items_details()

        # Verify Initial Cart Items
        self.logger.info(
            "Verifying selected items match the items in the cart."
        )

        assert selected_items == cart_items, (
            "Selected items and cart items do not match."
        )

        # Remove Items
        self.logger.info(
            f"Removing {remove_item_count} item(s) from the cart."
        )

        remaining_items = cart_page.remove_item_from_cart(
            remove_item_count,
            cart_items
        )

        # Verify Remaining Cart Items
        self.logger.info(
            "Verifying the remaining items in the cart."
        )

        cart_items_after_removal = (
            cart_page.get_cart_items_details()
        )

        assert remaining_items == cart_items_after_removal, (
            "Expected remaining items and actual cart items "
            "do not match."
        )

        # Verify Cart Badge After Removal
        expected_count = (
                int(add_item_to_cart_count)
                - int(remove_item_count)
        )

        self.logger.info(
            "Verifying the cart badge count after item removal."
        )

        badge_count = inventory_page.get_cart_badge_count()

        assert badge_count == str(expected_count), (
            f"Expected cart badge count {expected_count}, "
            f"but got {badge_count}."
        )

        # Continue Shopping
        self.logger.info(
            "Clicking the Continue Shopping button."
        )

        cart_page.click_continue_shopping_button()

        # Verify Cart Button Status
        self.logger.info(
            "Verifying the Add to Cart and Remove button states."
        )

        items_status = inventory_page.get_items_cart_button_status()

        remaining_item_names = [
            item["item_name"]
            for item in remaining_items
        ]

        for item in items_status:

            if item["item_name"] in remaining_item_names:

                assert item["button_text"] == "Remove", (
                    f"'{item['item_name']}' should show "
                    f"Remove button."
                )

            else:

                assert item["button_text"] == "Add to cart", (
                    f"'{item['item_name']}' should show "
                    f"Add to cart button."
                )
    @allure.story("Product detail page")
    @allure.title("TC-005: Open product page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that clicking a product opens its details page.")
    def test_item_click_open_product(self):
        self.logger.info(
            "Starting TC-005: Verify that clicking a product opens its details page."
        )

        inventory_page = self.login_to_inventory()

        # Open a random product
        self.logger.info(
            "Clicking on a random product to open the product details page."
        )

        selected_item_details, product_page = (
            inventory_page.open_product_page()
        )

        # Verify product details
        self.logger.info(
            "Verifying that the correct product details are displayed."
        )

        actual_item_details = product_page.get_item_details()

        assert selected_item_details == actual_item_details, (
            f"Product details mismatch!\n"
            f"Expected: {selected_item_details}\n"
            f"Actual: {actual_item_details}"
        )
