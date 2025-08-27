from selenium.webdriver.common.by import By

class Locators:

    # Basic Auth Locators
    username_id = (By.ID, "user-name")
    password_id = (By.ID, "password")
    btn_login_id = (By.ID, "login-button")
    #validasi error xpath
    username_empty_xpath = (By.XPATH, "//h3[normalize-space()='Epic sadface: Username is required']")
    password_empty_xpath = (By.XPATH, "//h3[normalize-space()='Epic sadface: Password is required']")
    locked_xpath = (By.XPATH, "//h3[@data-test='error']")
    fail_username_xpath = (By.XPATH, "//h3[@data-test='error']")
    fail_password_xpath = (By.XPATH, "//h3[@data-test='error']")

    # Logout Locators
    open_menu_xpath = (By.XPATH, "//button[normalize-space()='Open Menu']")
    btn_logout_xpath = (By.XPATH, "//a[@id='logout_sidebar_link']")