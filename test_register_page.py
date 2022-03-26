from pages.register_page import RegisterPage
import names


def test_guest_can_register(browser):
    link = "http://demowebshop.tricentis.com/register"
    register_page = RegisterPage(browser, link)
    register_page.open()
    register_page.should_be_register_page()
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    password = "12345678"
    email = first_name + last_name + "@fakemail.org"
    register_page.register_new_user(first_name, last_name, email, password)



