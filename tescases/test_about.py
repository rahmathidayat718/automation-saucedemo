from logger import logger
from pages.about_page import AboutPage
from pages.logout_page import LogoutPage
from utilities.read_properties import ReadConfig

class TestAbout:

    def test_about(self, driver, config):
        about_page = AboutPage(driver)
        driver.get(config["logout_url_page"])

        about_page.about()

        # URL Validation
        expected_url = ReadConfig.get_about_url_page()
        current_url = driver.current_url

        assert current_url == expected_url, f"URL tidak sesuai! Harusnya {expected_url}, tapi dapat {current_url}"
        logger.debug("validation about url")
        logger.info("=====> Logout Sauce Demo finished")