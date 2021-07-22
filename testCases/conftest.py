import pytest
from selenium import webdriver
import pytest


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\srikar\\PycharmProjects\\Drivers\\chromedriver.exe")
        print("Launching Chrome browser...........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser...........")
    else:
        driver = webdriver.Firefox()
        # driver = webdriver.Ie("C:\\Users\\srikar\\PycharmProjects\\Drivers\\IEDriverServer.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####HTML Report###
# HOOK for adding environment info#
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Srikar'


# HOOK for Delete/Modify environment info#
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
