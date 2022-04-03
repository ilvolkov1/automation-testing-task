from pages.register_page import RegisterPage
import names
import pytest
from testdata import TestUser


@pytest.mark.smoke
def test_guest_can_register(browser):
    link = RegisterPage.register_page_link
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    password = "12345678"
    email = first_name + last_name + "@fakemail.org"

    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.should_be_register_page()
    register_page.register_new_user(first_name, last_name, email, password)
    register_page.should_be_success_message()


def test_guest_cannot_register_with_existing_email(browser):
    link = RegisterPage.register_page_link
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    password = "12345678"
    email = TestUser.email

    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.should_be_register_page()
    register_page.register_new_user(first_name, last_name, email, password)
    register_page.should_be_message_about_email_already_exist()
