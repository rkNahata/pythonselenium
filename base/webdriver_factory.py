from selenium import webdriver
import os
import pytest


class WebDriverFactory():
    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):

        baseUrl = "https://letskodeit.teachable.com/"

        if self.browser == 'chrome':
            driverLocation = "/Users/mmt6198/Downloads/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
        elif self.browser == 'firefox':
            pass

        driver.implicitly_wait(3)

        driver.get(baseUrl)

        driver.maximize_window()

        return driver

    def pytest_addoption(parser):
        parser.pytest_addoption("--browser")

    @pytest.fixture(scope="class")
    def browser(self, request):
        return request.config.getoption("--browser")
