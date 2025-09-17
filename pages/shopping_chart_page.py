import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc
from logger import logger


class ShoppingChartPage(BaseDriver):

    def click_chart(self):
        self.click(Lc.icon_chart)
        logger.debug("click icon shopping chart")
        time.sleep(5)