import pytest
from generic.webdriverFactory import WebDriverFactory
from page_folder.UL import ULone
from generic.path import *
import os
from datetime import date
from datetime import datetime
import time




@pytest.yield_fixture()
def setUp():
    print("Running setUp for test case")
    yield
    print("Running tearDown for test case")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    ul = ULone(driver)
    #ul.login(VALID_EMAIL_LOGIN['email'], VALID_EMAIL_LOGIN['_password'])
    #ul.create_request()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    #print(" Running one time tearDown")


def pytest_addoption(parser):
      parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.yield_fixture()
def folder():
    today = date.today()
    print(today)
    time = datetime.now()
    print(time)

    file_path = ".\\Ascent_MDM"
    # directory = os.path.dirname(file_path)
    try:
        print(os.getcwd())
        if not os.path.exists(file_path):
            os.chdir("C:\\Users\\Hasher\\PycharmProjects\\Ascent_MDM")
            print("pass")
            os.mkdir(str(today))
            print(os.getcwd())
        else:
            print("path is already created")

    except OSError:
        print('Error: Creating directory. ' + file_path)


