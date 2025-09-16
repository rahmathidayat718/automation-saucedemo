from pages.filter_products_page import FilterProducts


class TestFilter:

    def test_filter(self, driver, config):
        filter_page = FilterProducts(driver)
        driver.get(config["logout_url_page"])
        filter_page.filter_products()