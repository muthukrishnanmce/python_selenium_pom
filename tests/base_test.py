import pytest

from utilities.driver_factory import DriverFactory


class TestBaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        driver_factory = DriverFactory()
        self.driver = driver_factory.get_driver_instance()

        yield self.driver
        method_name = request.node.name
        if request.node.rep_call.failed:
            print('test {} failed :('.format(method_name))
            # do more stuff like take a selenium screenshot
        self.driver.quit()