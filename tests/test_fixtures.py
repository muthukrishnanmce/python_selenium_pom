import pytest

from utilities.driver_factory import DriverFactory


@pytest.fixture()
def driver():
    driver_factory = DriverFactory()
    driver = driver_factory.get_driver_instance()
    yield driver
    driver.quit()
