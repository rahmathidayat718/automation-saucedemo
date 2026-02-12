from pages.shopping_chart_page import ShoppingChartPage
from pages.login_page import LoginPage
from utilities.read_properties import ReadConfig
from logger import logger


class TestShoppingChart:

    def test_shopping_chart(self, driver, config):
        login_page = LoginPage(driver)
        chart_page = ShoppingChartPage(driver)
        driver.get(config["login_url_page"])

        username, password = ReadConfig.get_data_for_login()
        login_page.login_user(username, password)

        chart_page.add_click_chart()

