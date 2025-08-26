from selenium import webdriver
import pytest
from utilities.read_properties import ReadConfig

#report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        if rep.failed:
            # biarkan error muncul normal
            rep.longrepr = str(rep.longrepr)
        else:
            # hilangkan detail log jika test pass
            rep.longrepr = None


@pytest.fixture()
def driver():
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get(ReadConfig.get_login_url_page())
    yield driver
    driver.quit()

@pytest.fixture()
def config():
    return{
        "login_url_page": ReadConfig.get_login_url_page(),
    }

# DATA LOGIN
@pytest.fixture(
    params=ReadConfig.get_data_login(),
    ids=lambda param: param[2]
)
def data_login(request):
    return request.param