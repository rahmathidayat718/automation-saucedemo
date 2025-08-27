from logger import logger
from pages.logout_page import LogoutPage
from utilities.read_properties import ReadConfig

class TestLogout:

    def test_logout(self, driver, config):
        logout_page = LogoutPage(driver)
        driver.get(config["logout_url_page"])

        logout_page.logout_user()

        # URL Validation
        expected_url = ReadConfig.get_after_logout_url()
        current_url = driver.current_url

        assert current_url == expected_url, f"URL tidak sesuai! Harusnya {expected_url}, tapi dapat {current_url}"
        logger.debug("validation logout url")
        logger.info("=====> Logout Sauce Demo finished")