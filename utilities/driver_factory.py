from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.test_config import TestConfig


class DriverFactory:

    def __init__(self):
        self.chrome_options = None
        self.driver = None

    def get_driver_instance(self):
        if self.driver is None:
            browser_name = TestConfig.get_config("browser")
            if browser_name.upper() == "CHROME":
                self.add_chrome_capabilities()
                self.driver = webdriver.Chrome(options=self.chrome_options)
        return self.driver

    def add_chrome_capabilities(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-extensions")

