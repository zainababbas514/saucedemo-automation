import random

from selenium.webdriver.common.by import By

from pages.checkout_page_one import CheckoutPageOne
from utils.base_class import BaseClass


class CartPage(BaseClass):

    cart_items_list = (By.CSS_SELECTOR, ".cart_list .cart_item")
    item_name = (By.CSS_SELECTOR, ".cart_item_label a")
    item_desc = (By.CSS_SELECTOR, ".inventory_item_desc")
    item_price = (By.CSS_SELECTOR, ".inventory_item_price")
    remove_buttons = (By.XPATH, "//button[normalize-space()='Remove']")
    continue_shopping_button = (By.CSS_SELECTOR, "button#continue-shopping")
    checkout_button = (By.CSS_SELECTOR, "button.checkout_button")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items_list(self):
        return self.find_elements(self.cart_items_list)

    def get_cart_items_details(self):
        items_list = []

        for item in self.get_cart_items_list():
            items_list.append({
                "item_name": item.find_element(*self.item_name).text,
                "item_desc": item.find_element(*self.item_desc).text,
                "item_price": float(
                    item.find_element(*self.item_price)
                    .text
                    .replace("$", "")
                )
            })

        return items_list

    def remove_item_from_cart(self, remove_count, cart_items_list):

        remove_count = int(remove_count)

        if remove_count > len(cart_items_list):
            raise ValueError(
                f"Cannot remove {remove_count} items. "
                f"Only {len(cart_items_list)} items are in the cart."
            )


        item_to_remove = random.sample(
            cart_items_list, remove_count
        )

        for item in item_to_remove:
            item_names_list = self.find_elements(self.item_name)
            remove_buttons = self.find_elements(self.remove_buttons)

            for index, item_name in enumerate(item_names_list):

                if item["item_name"] == item_name.text:
                    remove_buttons[index].click()
                    break

            # Remove item from stored list
            cart_items_list = [
                cart_item
                for cart_item in cart_items_list
                if cart_item["item_name"] != item["item_name"]
            ]

        return cart_items_list

    def click_continue_shopping_button(self):
        self.click(self.continue_shopping_button)

    def click_checkout_button(self):
        self.click(self.checkout_button)
        return CheckoutPageOne(self.driver)