import pytest
from selenium import webdriver
import names
import time
from pages.register_page import RegisterPage
from pages.locators import BasePageLocators
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options


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
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store', default=False,
                     help="You can run browser in headless way by adding 'True' option")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_option = request.config.getoption("headless")
    options_chrome = Options()
    options_firefox = firefox_options()
    if browser_option:
        options_chrome.headless = True
        options_firefox.headless = True

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

