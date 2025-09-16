import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc
from logger import logger

class FilterProducts(BaseDriver):

    def click_name_a_z(self):
        self.click(Lc.click_Name_A_Z)
        logger.debug(f"Click Sort By Name A-Z")
    def click_name_z_a(self):
        self.click(Lc.click_Name_Z_A)
        logger.debug(f"Click Sort By Name Z-A")
    def click_price_low_high(self):
        self.click(Lc.click_Price_Low_High)
        logger.debug(f"Click Sort By Price Low-High")
    def click_price_high_low(self):
        self.click(Lc.click_Price_High_Low)
        logger.debug(f"Click Sort By Price High-Low")

    def filter_products(self):
        self.click_name_a_z()
        time.sleep(5)
        self.click_name_z_a()
        time.sleep(5)
        self.click_price_low_high()
        time.sleep(5)
        self.click_price_high_low()