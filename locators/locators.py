from selenium.webdriver.common.by import By

class Locators:

    # Basic Auth Locators
    username_id = (By.ID, "user-name")
    password_id = (By.ID, "password")
    btn_login_id = (By.ID, "login-button")

    # Logout Locators
    open_menu_xpath = (By.XPATH, "//button[normalize-space()='Open Menu']")
    btn_logout_xpath = (By.XPATH, "//a[@id='logout_sidebar_link']")