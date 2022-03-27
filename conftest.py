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


@pytest.fixture(scope="function")
def browser():
    c = webdriver.ChromeOptions()
    c.add_argument("--incognito")
    browser = webdriver.Chrome(options=c)
    yield browser
    browser.quit()


