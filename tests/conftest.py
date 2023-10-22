import pytest
from selenium import webdriver

from utilities.driver_factory import DriverFactory
from utilities.screenshot_utils import ScreenShotUtils
from utilities.test_config import TestConfig
from pytest import StashKey, CollectReport
from typing import Dict
import time

phase_report_key = StashKey[Dict[str, CollectReport]]()


@pytest.fixture(scope='session')
def config():
    config = TestConfig()
    return config.get_config_data()

@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    rep = yield

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep

    return rep

@pytest.fixture()
def setup(request, config):
    driver_factory = DriverFactory()
    driver = driver_factory.get_driver_instance()
    driver.implicitly_wait(config["timeout"])
    request.cls.driver: webdriver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "chrome":
        driver.maximize_window()
    yield driver
    # if request.session.testsfailed != before_failed:
    #     print("test failed")
    #     ScreenShotUtils.take_standard_screenshot()
    #     # take and save screenshot
    # #     allure.attach(driver.get_screenshot_as_png(),
    # #                   name="Test failed", attachment_type=AttachmentType.PNG)
    report = request.node.stash[phase_report_key]
    if report["setup"].failed:
        print("setting up a test failed or skipped", request.node.nodeid)
    elif ("call" not in report) or report["call"].failed:
        print("executing test failed or skipped", request.node.nodeid)
        print("test failed: Capturing screenshot  ", request.node.nodeid)
        ScreenShotUtils.take_standard_screenshot(driver=driver,
                                                 file_name=f'test_runs/screenshots/{request.node.name}_{time.time_ns()}'
                                                           f'.png')
    driver.quit()


