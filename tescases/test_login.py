from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from logger import logger

class TestLogin:

    def test_login(self, driver, config, data_login):
        login_page = LoginPage(driver)
        driver.get(config["login_url_page"])

        username, password, section_name = data_login
        login_page.login_user(username, password)

        # URL Validation
        expected_url = ReadConfig.get_after_login_url()
        current_url = driver.current_url

        assert current_url == expected_url, f"URL tidak sesuai! Harusnya {expected_url}, tapi dapat {current_url}"
        logger.debug("Url validation")
        logger.info("=====> Login sequence finished")