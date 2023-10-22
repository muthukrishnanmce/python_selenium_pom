import pytest
from selenium.webdriver.common.by import By


# from tests.test_fixtures import driver

@pytest.mark.usefixtures("setup")
class TestFirstLoginTest:
    @pytest.fixture(autouse=True)
    def inital_setup(self, setup):
        self.driver = setup

    def test_login(self):
        self.driver.get("https://www.saucedemo.com/")
        assert self.driver.current_url == "https://www.saucedemo.com/"

    def test_login_fail(self):
        self.driver.get("https://www.saucedemo.com/")
        assert self.driver.current_url == "https://www.saucedemo.com??"

    def test_drag_and_drop_test(self):
        self.driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        gallery = self.driver.find_element(By.XPATH, "//ul[@id='gallery']")
        assert gallery.is_displayed()

