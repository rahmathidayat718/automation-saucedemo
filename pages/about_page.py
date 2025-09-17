import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc
from logger import logger

class AboutPage(BaseDriver):

    # Logout Action
    def click_open_menu(self):
        self.click(Lc.open_menu_xpath)
        logger.debug("Click Open Menu")

    def click_about(self):
        self.click(Lc.btn_about_xpath)
        logger.debug("Click Logout")

    # LOGIN AND LOGOUT
    def about(self):
        logger.info("=====> Start Logout Sauce demo")
        time.sleep(2)
        self.click_open_menu()
        time.sleep(2)
        self.click_about()