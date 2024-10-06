import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def browser():
    service = Service("/Users/alesyalu/PycharmProjects/driver/chromedriver-mac-arm64/chromedriver")
    browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    yield browser
    browser.quit()
