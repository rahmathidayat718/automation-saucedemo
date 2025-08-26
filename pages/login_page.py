import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc
from logger import logger

class LoginPage(BaseDriver):

    def enter_username(self, username):
        if username is None:
            username = ""
        logger.debug(f"Input username: '{username}'")
        self.enter_text(Lc.username_id, username)

    def enter_password(self, password):
        if password is None:
            password = ""
        logger.debug(f"Input password: {password}")
        self.enter_text(Lc.password_id, password)

    def click_btn_login(self):
        logger.debug("Click login button")
        self.click(Lc.btn_login_id)

    # LOGIN
    def login_user(self, username,password):
        logger.debug("Start login sequence")
        self.enter_username(username)
        self.enter_password(password)
        self.click_btn_login()
        time.sleep(2)
        logger.debug("Login sequence finished")