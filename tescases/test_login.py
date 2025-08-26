from pages.login_page import LoginPage


class TestLogin:

    def test_login(self, driver, config, data_login):
        login_page = LoginPage(driver)
        driver.get(config["login_url_page"])

        username, password, section_name = data_login
        login_page.login_user(username, password)