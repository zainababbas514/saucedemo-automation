import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from utils.base_class import BaseClass


class InventoryPage(BaseClass):

    inventory_items_list = (By.CSS_SELECTOR, ".inventory_list .inventory_item")
    item_image = (By.CSS_SELECTOR, ".inventory_item_img img")
    item_title = (By.CSS_SELECTOR, ".inventory_item_name")
    item_price = (By.CSS_SELECTOR, ".inventory_item_price")
    item_desc = (By.CSS_SELECTOR, ".inventory_item_desc")
    add_to_cart_btn = (By.CSS_SELECTOR, "button.btn_inventory")
    cart_badge = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    cart = (By.CSS_SELECTOR, "a.shopping_cart_link")
    sort_dropdown = (By.CSS_SELECTOR, "select.product_sort_container")

    # Sort dropdown options
    sort_by_az = "az"
    sort_by_za = "za"
    sort_by_low_high = "lohi"
    sort_by_high_low = "hilo"

    def __init__(self, driver):
        self.driver = driver

    def get_inventory_list(self):
        return self.find_elements(self.inventory_items_list)

    def get_inventory_items_details(self):
        items_details = []

        for item in self.get_inventory_list():

            image = item.find_element(*self.item_image)
            add_to_cart_button = item.find_element(*self.add_to_cart_btn)
            price = item.find_element(*self.item_price)
            name = item.find_element(*self.item_title)

            item_details = {
                "item_name": name.text,
                "item_desc": item.find_element(*self.item_desc).text,
                "item_price": price.text,
                "item_image": image.get_attribute("src"),
                "image_displayed": image.is_displayed(),
                "add_to_cart_displayed": add_to_cart_button.is_displayed(),
                "add_to_cart_enabled": add_to_cart_button.is_enabled(),
                "price_displayed": price.is_displayed(),
                "name_displayed": name.is_displayed()

            }

            items_details.append(item_details)

        return items_details

    def get_items_name_list(self):
        names = self.find_elements(self.item_title)
        return [item.text for item in names]

    def get_items_desc_list(self):
        return self.find_elements(self.item_desc)

    def get_items_price_list(self):
        prices = self.find_elements(self.item_price)
        return [float(item.text.replace("$", "")) for item in prices]

    def get_items_image_list(self):
        return self.find_elements(self.item_image)

    def add_items_to_cart(self, item_count):
        items_list = self.get_inventory_list()
        total_items = len(items_list)

        item_count = int(item_count)

        if item_count > total_items:
            raise ValueError(
                f"Cannot add {item_count} items. "
                f"Only {total_items} items are available."
            )

        random_indexes = random.sample(
            range(total_items),
            item_count
        )

        cart_items = []

        for index in random_indexes:
            item = items_list[index]

            item.find_element(*self.add_to_cart_btn).click()

            item_name = item.find_element(*self.item_title).text
            item_desc = item.find_element(*self.item_desc).text
            item_price = item.find_element(*self.item_price).text

            cart_item = {
                "item_name": item_name,
                "item_desc": item_desc,
                "item_price": float(item_price.replace("$", ""))
            }

            cart_items.append(cart_item)

        return cart_items

    def get_cart_badge_count(self):
        return self.get_text(self.cart_badge)

    def open_cart_page(self):
        self.click(self.cart)
        return CartPage(self.driver)

    def get_items_cart_button_status(self):
        items_status = []

        for item in self.get_inventory_list():

            item_name = item.find_element(*self.item_title).text
            button_text = item.find_element(*self.add_to_cart_btn).text

            items_status.append({
                "item_name": item_name,
                "button_text": button_text
            })

        return items_status

    def open_product_page(self):
        items_list = self.get_inventory_list()

        selected_item = random.choice(items_list)

        item_details = {
            "item_name": selected_item.find_element(*self.item_title).text,
            "item_desc": selected_item.find_element(*self.item_desc).text,
            "item_price": float(
                selected_item.find_element(*self.item_price)
                .text
                .replace("$", "")
            ),
            "item_image": selected_item.find_element(
                *self.item_image
            ).get_attribute("src")
        }

        selected_item.find_element(*self.item_title).click()

        return item_details, ProductPage(self.driver)

    def sort_items(self, sort_option):
        dropdown = Select(self.find_element(self.sort_dropdown))
        dropdown.select_by_value(sort_option)