# SauceDemo Automation

A Selenium WebDriver automation project for testing the SauceDemo web application using Python, Pytest, and the Page Object Model (POM).

## 🧪 Project Overview

This project automates key e-commerce workflows of the SauceDemo application, including product validation, cart management, product sorting, product details, and the complete checkout process.

The framework uses:

* Page Object Model (POM)
* Pytest fixtures
* Explicit waits
* External JSON test data
* Parameterized tests
* Allure reporting
* Logging
* Multi-browser execution

## 🛠️ Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)
* JSON
* Allure

## 📋 Test Coverage

* Product list, name, image, and price validation
* Add single and multiple products to cart
* Cart item validation
* Remove products from cart
* Product details page validation
* Product sorting by name (A-Z / Z-A)
* Product sorting by price (Low-High / High-Low)
* Complete product checkout flow
* Subtotal, tax, and total amount validation
* Order confirmation validation
* Multi-browser execution: Chrome, Firefox, Edge
* Failure screenshot capture
* Allure reporting
* Logging

## 📁 Project Structure

```text
saucedemo-automation/
├── pages/
├── testCases/
├── testData/
├── tests/
├── utils/
├── conftest.py
├── .gitignore
└── README.md
```

The manually documented test cases are available in the `testCases` folder.

## ▶️ Run Tests

Install dependencies:

```bash
pip install selenium pytest allure-pytest requests
```

Run all tests:

```bash
pytest
```

Run tests with a specific browser:

```bash
pytest --browser=chrome
pytest --browser=firefox
pytest --browser=edge
```

## 📊 Allure Reports

Generate Allure test results while running the tests:

```bash
pytest --alluredir=allure-results
```

Generate the Allure HTML report:

```bash
allure generate allure-results -o allure-report --clean
```

Open the generated report:

```bash
allure open allure-report
```

Alternatively, you can generate and open the report directly:

```bash
allure serve allure-results
```

`allure serve` creates a temporary HTML report and opens it in the browser.

## 🌐 Application

**SauceDemo:**
https://www.saucedemo.com/

## 📌 Framework Highlights

* Page Object Model for maintainable and reusable test code
* Explicit waits for synchronization
* External JSON test data
* Pytest fixtures and parameterization
* Multi-browser support
* Automatic screenshots on test failure
* Allure reporting
* Logging
* Reusable BaseClass utilities
