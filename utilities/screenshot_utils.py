class ScreenShotUtils:
    @staticmethod
    def take_standard_screenshot(driver, file_name):
        driver.save_screenshot(file_name)