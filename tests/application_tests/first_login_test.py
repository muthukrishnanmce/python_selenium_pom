import pytest

# from tests.test_fixtures import driver

@pytest.mark.usefixtures("setup")
class TestFirstLoginTest:

    def test_login(self):
        self.driver.get("https://www.saucedemo.com/")
        assert self.driver.current_url == "https://www.saucedemo.com/"