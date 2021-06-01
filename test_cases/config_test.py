import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    if browser == 'chrome' or 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox' or 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # this will get the value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to set up method
    return request.config.getoption("--browser")



# To run the test case execute below command in terminal
# "pytest -v -s <relative path of the .py test case file> --browser <chrome/firefox>"
# To run two ifferent test cases simultaniously we use below command
# "pytest -v -s -n=<number of methods> <relative path of the .py test case file> --browser <chrome/firefox>"