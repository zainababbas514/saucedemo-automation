from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage
from utils.base_class import BaseClass


class LoginPage(BaseClass):

    username_input = (By.XPATH, "//input[@name='user-name']")
    password_input = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//input[@name='login-button']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.submit_button)
        return InventoryPage(self.driver)


