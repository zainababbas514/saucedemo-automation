from selenium.webdriver.common.by import By
from pages.checkout_page_two import CheckoutPageTwo
from utils.base_class import BaseClass


class CheckoutPageOne(BaseClass):

    first_name_input = (By.CSS_SELECTOR, "input#first-name")
    last_name_input = (By.CSS_SELECTOR, "input#last-name")
    postal_code_input = (By.CSS_SELECTOR, "input#postal-code")
    continue_button = (By.CSS_SELECTOR, "input#continue")

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, name):
        self.send_keys(self.first_name_input, name)

    def enter_last_name(self, lastname):
        self.send_keys(self.last_name_input, lastname)

    def enter_postal_code(self, code):
        self.send_keys(self.postal_code_input, code)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def click_continue_button(self):
        self.click(self.continue_button)
        return CheckoutPageTwo(self.driver)

