import time
from pages.change_password_page import ChangePasswordPage
from pages.login_page import LoginPage
from testdata import TestUser
import pytest


@pytest.mark.smoke
def test_user_can_change_password(browser):
    login_link = LoginPage.login_page_link
    change_password_link = ChangePasswordPage.change_password_page_link
    email = TestUser.email
    password = TestUser.password
    new_password = password*2

    login_page = LoginPage(browser, login_link)
    login_page.open()
    login_page.log_in(email, password)

    change_password_page = ChangePasswordPage(browser, change_password_link)
    change_password_page.open()
    change_password_page.should_be_change_password_page()
    change_password_page.change_password(password, new_password)
    change_password_page.should_be_success_message()
    change_password_page.open()
    change_password_page.change_password(new_password, password)


def test_user_should_see_warning_message_about_wrong_old_password(browser):
    login_link = LoginPage.login_page_link
    change_password_link = ChangePasswordPage.change_password_page_link
    email = TestUser.email
    password = TestUser.password
    new_password = "!"+password

    login_page = LoginPage(browser, login_link)
    login_page.open()
    login_page.log_in(email, password)

    change_password_page = ChangePasswordPage(browser, change_password_link)
    change_password_page.open()
    change_password_page.should_be_change_password_page()
    change_password_page.change_password(new_password, new_password)
    change_password_page.should_be_warning_message_about_wrong_old_password()
