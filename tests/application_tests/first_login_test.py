import pytest

from tests.base_test import TestBaseTest


class TestFirstLoginTest(TestBaseTest):

    def test_login(self):
        self.driver.get("https://www.saucedemo.com/")
        assert self.driver.current_url == "https://www.saucedemo.com/"