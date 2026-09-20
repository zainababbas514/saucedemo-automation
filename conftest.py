import os

import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver


load_dotenv()

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome, firefox, or edge)"
    )


@pytest.fixture
def init_browser(request):
    global driver

    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference(
            "browser.privatebrowsing.autostart",
            True
        )
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--inprivate")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(
            f"Browser '{browser}' is not supported"
        )

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.quit()


@pytest.fixture
def login_credentials():
    username = os.getenv("SAUCE_USERNAME")
    password = os.getenv("SAUCE_PASSWORD")

    if not username or not password:
        raise ValueError(
            "SAUCE_USERNAME and SAUCE_PASSWORD must be set in the .env file"
        )

    return {
        "username": username,
        "password": password
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, "driver", None)

        if driver:
            screenshot = driver.get_screenshot_as_png()

            allure.attach(
                screenshot,
                name=f"{item.name} Screenshot",
                attachment_type=allure.attachment_type.PNG
            )