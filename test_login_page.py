import time
from pages.login_page import LoginPage
from testdata import TestUser
import pytest


@pytest.mark.smoke
def test_user_can_log_in(browser):
    link = LoginPage.login_page_link
    email = TestUser.email
    password = TestUser.password
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()
    login_page.log_in(email, password)
    login_page.should_be_logged_in(email)
