import time
from pages.change_password_page import ChangePasswordPage
from pages.login_page import LoginPage


def test_user_can_change_password(browser, create_new_user):
    login_link = "http://demowebshop.tricentis.com/login"
    change_password_link = "http://demowebshop.tricentis.com/customer/changepassword"
    data = create_new_user
    email = data[0]
    password = data[1]
    new_password = password*2

    login_page = LoginPage(browser, login_link)
    login_page.open()
    login_page.log_in(email, password)

    change_password_page = ChangePasswordPage(browser, change_password_link)
    change_password_page.open()
    change_password_page.should_be_change_password_page()
    change_password_page.change_password(password, new_password)
    change_password_page.should_be_success_message()
