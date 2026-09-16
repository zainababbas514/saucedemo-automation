import requests
from selenium.webdriver.common.by import By
from utils.base_class import BaseClass


class ProductPage(BaseClass):

    item_image = (By.CSS_SELECTOR, ".inventory_details_img")
    item_name = (By.CSS_SELECTOR, ".inventory_details_name")
    item_desc = (By.CSS_SELECTOR, ".inventory_details_desc")
    item_price = (By.CSS_SELECTOR, ".inventory_details_price")

    def __init__(self, driver):
        self.driver = driver

    def get_item_details(self):
        return  {
            "item_name": self.find_element(self.item_name).text,
            "item_desc": self.find_element(self.item_desc).text,
            "item_image": self.get_attribute(self.item_image, "src"),
            "item_price": float(
                self.find_element(self.item_price).text.replace("$", "")
            )
        }

    def get_image_status_code(self):
        image_url = self.get_attribute(self.item_image, "src")
        response = requests.get(image_url, timeout=10)
        return response.status_code