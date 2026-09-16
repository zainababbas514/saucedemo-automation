import inspect
import json
import logging
import os
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseClass:
    WAIT_TIMEOUT = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(EC.visibility_of_all_elements_located(locator))

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        element = WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def wait_for_url(self, expected_url):
        try:
            WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
                EC.url_to_be(expected_url)
            )
        except TimeoutException:
            actual_url = self.driver.current_url
            raise AssertionError(
                f"Expected URL '{expected_url}', "
                f"but got '{actual_url}'"
            )

    def is_element_visible(self, locator):
        return self.find_element(locator).is_displayed()

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)


    @staticmethod
    def get_logger():
        log_path = f"logs/saucedemo_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            file_handler = logging.FileHandler(log_path)

            console_handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

    @staticmethod
    def get_data_from_json(filename, key=None):
        file_path = os.path.abspath(os.path.join("testData", filename))
        with open(file_path, "r") as f:
            data = json.load(f)
        return data[key] if key else data


