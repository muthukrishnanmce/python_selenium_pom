import pytest

from utilities.driver_factory import DriverFactory


class TestBaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        driver_factory = DriverFactory()
        self.driver = driver_factory.get_driver_instance()

        yield self.driver
        self.driver.quit()