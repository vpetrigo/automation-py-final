import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--language", default="en", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language_to_use = request.config.getoption("language")
    options = ChromeOptions()
    options.add_argument(f"--lang={language_to_use}")

    if os.getenv("TRAVIS") is not None:
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()
