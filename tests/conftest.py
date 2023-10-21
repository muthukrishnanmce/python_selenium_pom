import pytest

from utilities.driver_factory import DriverFactory
from utilities.test_config import TestConfig


@pytest.fixture(scope='session')
def config():
    config = TestConfig()
    return config.get_config_data()


@pytest.fixture()
def setup(request, config):
    driver_factory = DriverFactory()
    driver = driver_factory.get_driver_instance()
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "chrome":
        driver.maximize_window()
    yield
    if request.session.testsfailed != before_failed:
        print("test failed")
    #     allure.attach(driver.get_screenshot_as_png(),
    #                   name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()