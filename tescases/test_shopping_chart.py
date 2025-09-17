from pages.shopping_chart_page import ShoppingChartPage
from pages.login_page import LoginPage


class TestShoppingChart:

    def test_shopping_chart(self, driver, config, data_for_login):
        driver.get(config["login_url_page"])
        login_page = LoginPage(driver)
        chart_page = ShoppingChartPage(driver)

        username, password = data_for_login
        login_page.login_user(username, password)

        chart_page.click_chart()