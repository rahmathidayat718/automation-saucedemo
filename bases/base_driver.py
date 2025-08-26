from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.common import TimeoutException

class BaseDriver:

    driver = WebDriver

    def __init__(self, driver):
            self.driver = driver

    def find_element(self, locator, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                e.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            print(f"Elemen dengan locator {locator} tidak ditemukan dalam {timeout} detik.")
            return None

    def enter_text(self, locator, text, timeout=10):
        try:
            element = self.find_element(locator, timeout)
            if element:
                element.clear()
                element.send_keys(text)
                return element
            else:
                print(f"Elemen dengan locator {locator} tidak ditemukan untuk memasukkan teks.")
                return None
        except Exception as ee:
            print(f"Terjadi kesalahan saat mencoba memasukkan teks ke elemen: {ee}")
            return None
    def click(self, locator):
        self.find_element(locator).click()