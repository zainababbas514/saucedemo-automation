import allure
import pytest

from pages.login_page import LoginPage
from utils.base_class import BaseClass


@pytest.mark.usefixtures("init_browser")
@allure.feature("Order Products")
class TestOrder(BaseClass):

    logger = BaseClass.get_logger()
    data = BaseClass.get_data_from_json("data.json")

    @allure.story("Complete Order Flow")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC-010: Complete Product Purchase")
    @allure.description(
        "This test verifies that a user can add products to the cart, "
        "complete the checkout process with correct item details and totals, "
        "and see the order confirmation messages after proceeding with the checkout."
    )
    def test_order_items(self, login_credentials):

        self.logger.info(
            "Starting TC-010: Verify user can successfully complete an order."
        )

        # Initialize Login Page
        login_page = LoginPage(self.driver)

        # Test Data
        test_data = self.data["TC-010"]

        first_name = test_data["checkout_form"]["first_name"]
        last_name = test_data["checkout_form"]["last_name"]
        postal_code = test_data["checkout_form"]["postal_code"]

        expected_thank_you_message = test_data["thank_you_message"]
        expected_delivery_message = test_data["delivery_message"]
        add_item_to_cart_count = test_data["add_to_cart_item_count"]

        # Login
        self.logger.info(
            "Logging in with configured test credentials."
        )

        inventory_page = login_page.login(
            login_credentials["username"],
            login_credentials["password"]
        )

        self.logger.info(
            "Verifying the Inventory page is loaded."
        )

        assert "inventory.html" in inventory_page.get_current_url(), (
            "Inventory page was not loaded."
        )

        # Add Items
        self.logger.info(
            f"Adding {add_item_to_cart_count} item(s) to the cart."
        )

        selected_items = inventory_page.add_items_to_cart(
            add_item_to_cart_count
        )

        # Cart Page
        self.logger.info(
            "Opening the cart page."
        )

        cart_page = inventory_page.open_cart_page()
        cart_items = cart_page.get_cart_items_details()

        self.logger.info(
            "Verifying selected items match the items in the cart."
        )

        assert selected_items == cart_items, (
            "Selected items and the items in the cart do not match."
        )

        # Checkout Step 1
        self.logger.info(
            "Clicking the Checkout button."
        )

        checkout_page_one = cart_page.click_checkout_button()

        self.logger.info(
            "Filling the checkout form."
        )

        checkout_page_one.fill_checkout_form(
            first_name,
            last_name,
            postal_code
        )

        # Checkout Step 2
        self.logger.info(
            "Clicking the Continue button."
        )

        checkout_page_two = checkout_page_one.click_continue_button()

        checkout_items = checkout_page_two.get_checkout_items_details()

        self.logger.info(
            "Verifying selected items match the checkout items."
        )

        assert checkout_items == selected_items, (
            "Selected items and the items on the checkout page do not match."
        )

        # Verify Subtotal
        self.logger.info(
            "Verifying the checkout subtotal."
        )

        expected_subtotal = (
            checkout_page_two.calculate_expected_subtotal(
                selected_items
            )
        )

        actual_subtotal = checkout_page_two.get_item_total()

        assert actual_subtotal == expected_subtotal, (
            f"Expected subtotal {expected_subtotal}, "
            f"but got {actual_subtotal}."
        )

        # Verify Total
        self.logger.info(
            "Verifying the checkout total."
        )

        tax = checkout_page_two.get_tax_amount()
        actual_total = checkout_page_two.get_total()

        expected_total = round(actual_subtotal + tax, 2)

        assert actual_total == expected_total, (
            f"Expected total {expected_total}, "
            f"but got {actual_total}."
        )

        # Finish Order
        self.logger.info(
            "Completing the order."
        )

        order_success_page = checkout_page_two.click_finish_button()

        # Verify Order Confirmation
        self.logger.info(
            "Verifying the order confirmation message."
        )

        actual_thank_you_message = (
            order_success_page.get_thank_you_message()
        )

        assert actual_thank_you_message == expected_thank_you_message, (
            "Thank You message does not match."
        )

        self.logger.info(
            "Verifying the order delivery message."
        )

        actual_delivery_message = (
            order_success_page.get_order_delivery_message()
        )

        assert actual_delivery_message == expected_delivery_message, (
            "Delivery message does not match."
        )

        # Back to Inventory
        self.logger.info(
            "Clicking the Back Home button."
        )

        order_success_page.click_back_home_button()

        self.logger.info(
            "Verifying redirection to the Inventory page."
        )

        assert "inventory.html" in self.driver.current_url, (
            "User was not redirected to the Inventory page."
        )