import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc
from logger import logger

class LoginPage(BaseDriver):

    def enter_username(self, username):
        if username is None:
            username = ""
        self.enter_text(Lc.username_id, username)
        logger.debug(f"Input username: '{username}'")

    def enter_password(self, password):
        if password is None:
            password = ""
        self.enter_text(Lc.password_id, password)
        logger.debug(f"Input password: {password}")

    def click_btn_login(self):
        self.click(Lc.btn_login_id)
        logger.debug("Click login button")

    # LOGIN
    def login_user(self, username,password):
        logger.info("=====> Start login sequence")
        self.enter_username(username)
        self.enter_password(password)
        self.click_btn_login()
        time.sleep(2)