from selenium import webdriver
import pytest
from utilities.read_properties import ReadConfig
from pytest_metadata.plugin import metadata_key

#report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        if rep.failed:
            rep.longrepr = str(rep.longrepr)
        else:
            rep.longrepr = None

def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'SAUCE DEMO'
    config.stash[metadata_key] ['Tester Name'] = 'Rahmat Hidayat'


@pytest.fixture()
def driver():
    driver =webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def config():
    return{
        "login_url_page": ReadConfig.get_login_url_page(),
        "logout_url_page": ReadConfig.get_logout_url_page(),
    }

# DATA LOGIN
@pytest.fixture(
    params=ReadConfig.get_data_login(),
    ids=lambda param: param[2]
)
def data_login(request):
    return request.param