import time

from pages.login_page import LoginPage
from pages.register_page import RegisterPage
import names


def create_new_user(browser):
    link = "http://demowebshop.tricentis.com/register"
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    password = "12345678"
    email = first_name + last_name + "@fakemail.org"

    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.register_new_user(first_name, last_name, email, password)
    return email, password


def test_user_can_log_in(browser):
    link = "http://demowebshop.tricentis.com/login"
    data = create_new_user(browser)
    email = data[0]
    password = data[1]
    time.sleep(2)

    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()
    login_page.log_in(email, password)
    login_page.should_be_logged_in(email)
    time.sleep(2)
