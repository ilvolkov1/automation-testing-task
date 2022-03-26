from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.url, "This is not Login Page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_TEXT_FIELD), "Can't find Login Email text field"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_TEXT_FIELD), "Can't find Login Password text field"

    def log_in(self, email, password):
        self.get_page_element(*LoginPageLocators.EMAIL_TEXT_FIELD).send_keys(email)
        self.get_page_element(*LoginPageLocators.PASSWORD_TEXT_FIELD).send_keys(password)
        self.get_page_element(*LoginPageLocators.LOGIN_BUTTON).click()
