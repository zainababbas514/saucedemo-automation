from selenium.webdriver.common.by import By

from utils.base_class import BaseClass


class OrderSuccessPage(BaseClass):

    back_home_button = (By.CSS_SELECTOR, "button#back-to-products")
    order_delivery_message = (By.CSS_SELECTOR, "div.complete-text")
    thank_you_message = (By.CSS_SELECTOR, "h2.complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_thank_you_message(self):
        return self.get_text(self.thank_you_message)

    def get_order_delivery_message(self):
        return self.get_text(self.order_delivery_message)

    def click_back_home_button(self):
        self.click(self.back_home_button)