import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc
from logger import logger

class FilterProducts(BaseDriver):

    def click_name_a_z(self):
        self.click(Lc.click_Name_A_Z)
    def click_name_z_a(self):
        self.click(Lc.click_Name_A_Z)
    def click_price_low_high(self):
        self.click(Lc.click_Name_A_Z)
    def click_price_high_low(self):
        self.click(Lc.click_Name_A_Z)

    def filter_products(self):
        self.click_name_a_z()
        time.sleep(4)
        self.click_name_z_a()
        time.sleep(4)
        self.click_price_low_high()
        time.sleep(4)
        self.click_price_high_low()