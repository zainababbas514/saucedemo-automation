# SauceDemo Automation

A Selenium WebDriver automation project for testing the SauceDemo web application using Python, Pytest, and the Page Object Model (POM).

## 🧪 Project Overview

This project automates key e-commerce workflows of the SauceDemo application, including product validation, cart management, product sorting, product details, and the complete checkout process.

The framework is designed with reusable Page Objects, common Selenium utilities, external test data, Pytest fixtures, parameterization, logging, screenshots, and Allure reporting.

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **Allure**
* **JSON**
* **Requests**

## 📋 Test Coverage

The project covers the following scenarios:

* Verify products displayed on the Inventory page
* Add a single product to the cart
* Add multiple products to the cart
* Verify products displayed in the Cart
* Remove products from the Cart
* Verify product details page
* Sort products by name (A-Z)
* Sort products by name (Z-A)
* Sort products by price (Low to High)
* Sort products by price (High to Low)
* Complete checkout and order placement
* Verify subtotal, tax, and total amount
* Verify order confirmation messages
* Verify navigation back to the Inventory page

## ✨ Framework Features

* Page Object Model for reusable and maintainable test code
* Pytest fixtures for browser setup and teardown
* Parameterized tests for different test data
* Explicit waits for better synchronization
* External JSON test data
* Multi-browser execution
* Automatic screenshots on test failure
* Logging
* Allure reporting
* Reusable common Selenium methods through `BaseClass`
* HTTP validation for product image resources

## 📁 Project Structure

```text
saucedemo-automation/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page_one.py
│   ├── checkout_page_two.py
│   └── order_success_page.py
│
├── testCases/
│   └── test_cases.xlsx
│
├── testData/
│   └── data.json
│
├── tests/
│   ├── test_inventory_cart.py
│   ├── test_sorting.py
│   └── test_order.py
│
├── utils/
│   └── base_class.py
│
├── screenshots/
├── reports/
├── logs/
├── allure-results/
├── allure-report/
│
├── conftest.py
├── .gitignore
└── README.md
```

> Generated folders such as screenshots, logs, reports, and Allure results are excluded from version control through `.gitignore`.

## 🚀 Setup

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd saucedemo-automation
```

Install the required Python packages:

```bash
pip install selenium pytest allure-pytest requests
```

## ▶️ Running Tests

Run the complete test suite:

```bash
pytest
```

Run tests using a specific browser:

```bash
pytest --browser=chrome
```

```bash
pytest --browser=firefox
```

```bash
pytest --browser=edge
```

## 📊 Allure Reporting

Run the tests and generate Allure result files:

```bash
pytest --alluredir=allure-results
```

Generate the HTML report:

```bash
allure generate allure-results -o allure-report --clean
```

Open the generated report:

```bash
allure open allure-report
```

### Quick option

You can also generate and open a temporary Allure report directly:

```bash
allure serve allure-results
```

`allure serve` starts a local server and opens the report in the browser.

## 🧪 Test Data

Test data is maintained separately in:

```text
testData/data.json
```

This includes data such as:

* Login credentials
* Number of products to add to the cart
* Number of products to remove
* Checkout information

Separating test data from test logic makes the tests easier to maintain and update.

## 📸 Failure Screenshots

Screenshots are automatically captured when a test fails.

The screenshots are attached to the Allure report and can also be stored in the project's screenshot directory depending on the test configuration.

## 📝 Test Case Documentation

Detailed manual test scenarios are documented in:

```text
testCases/
```

The test cases cover inventory, cart, sorting, product details, and checkout functionality.

## 🌐 Application Under Test

**SauceDemo**

https://www.saucedemo.com/

## 🔧 Browser Support

The framework supports:

* Chrome
* Firefox
* Edge

Browser selection can be controlled through the Pytest command-line option:

```bash
pytest --browser=<browser>
```

Example:

```bash
pytest --browser=chrome
```
