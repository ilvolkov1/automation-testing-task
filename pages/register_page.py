from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()

    def should_be_register_url(self):
        assert "register" in self.url, "This is not Register Page"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.FIRST_NAME_TEXT_FIELD), "Can't find Register first name text field"
        assert self.is_element_present(*RegisterPageLocators.LAST_NAME_TEXT_FIELD), "Can't find Register last name text field"
        assert self.is_element_present(*RegisterPageLocators.EMAIL_TEXT_FIELD), "Can't find Register email text field"
        assert self.is_element_present(*RegisterPageLocators.PASSWORD_TEXT_FIELD), "Can't find Register password text field"
        assert self.is_element_present(*RegisterPageLocators.CONFIRM_PASSWORD_TEXT_FIELD), "Can't find Register password confirmation text field"

    def register_new_user(self, first_name, last_name, email, password):
        self.get_page_element(*RegisterPageLocators.FIRST_NAME_TEXT_FIELD).send_keys(first_name)
        self.get_page_element(*RegisterPageLocators.LAST_NAME_TEXT_FIELD).send_keys(last_name)
        self.get_page_element(*RegisterPageLocators.EMAIL_TEXT_FIELD).send_keys(email)
        self.get_page_element(*RegisterPageLocators.PASSWORD_TEXT_FIELD).send_keys(password)
        self.get_page_element(*RegisterPageLocators.CONFIRM_PASSWORD_TEXT_FIELD).send_keys(password)
        self.get_page_element(*RegisterPageLocators.REGISTER_BUTTON).click()