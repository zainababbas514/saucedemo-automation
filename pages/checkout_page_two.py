from selenium.webdriver.common.by import By

from pages.order_success_page import OrderSuccessPage
from utils.base_class import BaseClass


class CheckoutPageTwo(BaseClass):

    checkout_items_list = (By.CSS_SELECTOR, ".cart_list .cart_item")
    item_name = (By.CSS_SELECTOR, ".cart_item_label a")
    item_desc = (By.CSS_SELECTOR, ".inventory_item_desc")
    item_price = (By.CSS_SELECTOR, ".inventory_item_price")
    item_total = (By.CSS_SELECTOR, ".summary_subtotal_label")
    tax_amount = (By.CSS_SELECTOR, ".summary_tax_label")
    finish_button = (By.CSS_SELECTOR, "button#finish")
    total_amount = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def get_checkout_items_list(self):
        return self.find_elements(self.checkout_items_list)

    def get_checkout_items_details(self):
        items_list = []

        for item in self.get_checkout_items_list():
            item_detail = {
                "item_name": item.find_element(*self.item_name).text,
                "item_desc": item.find_element(*self.item_desc).text,
                "item_price": float(
                    item.find_element(*self.item_price)
                    .text
                    .replace("$", "")
                )
            }

            items_list.append(item_detail)

        return items_list

    def calculate_expected_subtotal(self, selected_items):
        return sum(item["item_price"] for item in selected_items)

    def get_item_total(self):
        item_total = self.get_text(self.item_total)
        return float(item_total.split("$")[1])

    def get_tax_amount(self):
        tax_amount = self.get_text(self.tax_amount)
        return float(tax_amount.split("$")[1])

    def get_total(self):
        total = self.get_text(self.total_amount)
        return float(total.split("$")[1])

    def click_finish_button(self):
        self.click(self.finish_button)
        return OrderSuccessPage(self.driver)