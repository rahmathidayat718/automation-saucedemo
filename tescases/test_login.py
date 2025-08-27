from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from logger import logger
from locators.locators import Locators as Lc
from selenium.common.exceptions import NoSuchElementException

class TestLogin:

    def test_login(self, driver, config, data_login):
        login_page = LoginPage(driver)
        driver.get(config["login_url_page"])

        username, password, section_name = data_login
        login_page.login_user(username, password)

        # URL Validation
        expected_url = ReadConfig.get_after_login_url()
        current_url = driver.current_url

        # STEP 1: Validasi URL
        if current_url == expected_url:
            logger.info("✅ Login berhasil: URL sesuai")
            assert True  # Langsung lulus test karena login berhasil
            return
        else:
            logger.warning(f"⚠ URL tidak sesuai! Harus: {expected_url}, tapi dapat: {current_url}")
            logger.info("➡ Login gagal, lanjut validasi pesan error...")

        # STEP 2: Validasi pesan error
        error_messages = [
            (Lc.username_empty_xpath, ReadConfig.get_error_username_empty()),
            (Lc.password_empty_xpath, ReadConfig.get_error_password_empty()),
            (Lc.locked_xpath, ReadConfig.get_error_locked()),
            (Lc.fail_username_xpath, ReadConfig.get_error_fail_username()),
            (Lc.fail_password_xpath, ReadConfig.get_error_fail_password())
        ]

        found_match = False
        for xpath, expected_text in error_messages:
            try:
                element = driver.find_element(*xpath)
                actual_text = element.text.strip()
                if actual_text == expected_text:
                    logger.info(f"✅ Pesan error sesuai: '{actual_text}'")
                    found_match = True
                    break
                else:
                    logger.debug(f"❌ Pesan error tidak cocok. Dapat: '{actual_text}', Harus: '{expected_text}'")
            except NoSuchElementException:
                logger.debug(f"❌ Elemen dengan xpath {xpath} tidak ditemukan.")

        # STEP 3: Assert sesuai hasil validasi
        assert found_match, f"❌ Login gagal, tetapi tidak ada pesan error yang sesuai. URL sekarang: {current_url}"
