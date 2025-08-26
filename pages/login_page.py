import time
from bases.base_driver import BaseDriver
from locators.locators import Locators as Lc


class LoginPage(BaseDriver):

    def enter_username(self, username):
        if username is None:
            username = ""
        self.enter_text(Lc.username_id, username)

    def enter_password(self, password):
        if password is None:
            password = ""
        self.enter_text(Lc.password_id, password)

    def click_btn_login(self):
        self.click(Lc.btn_login_id)

    # LOGIN
    def login_user(self, username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_btn_login()
        time.sleep(2)