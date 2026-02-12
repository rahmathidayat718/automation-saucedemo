import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc
from logger import logger


class ShoppingChartPage(BaseDriver):

    def click_chart(self):
        self.click(Lc.icon_chart)
        logger.debug("click icon shopping chart")
        time.sleep(5)

    def add_product(self):
        self.click(Lc.product1)
        logger.debug("Add Sauce Labs Backpack")
        time.sleep(2)
        self.click(Lc.product2)
        logger.debug("Sauce Labs Bike Light")
        time.sleep(2)
        self.click(Lc.product3)
        logger.debug("Sauce Labs Fleece Jacket")
        time.sleep(2)
        self.click(Lc.product4)
        logger.debug("Sauce Labs Onesie")
        time.sleep(2)

    def add_click_chart(self):
        self.add_product()
        self.click_chart()