import time
from pages.login_page import LoginPage


def test_user_can_log_in(browser, create_new_user):
    link = "http://demowebshop.tricentis.com/login"
    data = create_new_user
    email = data[0]
    password = data[1]
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()
    login_page.log_in(email, password)
    login_page.should_be_logged_in(email)
