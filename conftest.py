import pytest
from selenium import webdriver
import names
import time
from pages.register_page import RegisterPage
from pages.locators import BasePageLocators


@pytest.fixture(scope="function")
def create_new_user(browser):
    link = "http://demowebshop.tricentis.com/register"
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    password = "12345678"
    email = first_name + last_name + "@fakemail.org"
    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.register_new_user(first_name, last_name, email, password)
    register_page.get_page_element(*BasePageLocators.LOGOUT_LINK).click()
    return email, password


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

