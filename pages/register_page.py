from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):
    register_page_link = "http://demowebshop.tricentis.com/register"

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

    def should_be_success_message(self):
        assert "Your registration completed" in self.get_page_element(*RegisterPageLocators.REGISTER_SUCCESS_MESSAGE).text, "No success message"

    def should_be_message_about_email_already_exist(self):
        assert "The specified email already exists" in self.get_page_element(*RegisterPageLocators.EXISTING_EMAIL_MESSAGE).text, "No warning message"

    def fill_first_name(self, first_name):
        self.get_page_element(*RegisterPageLocators.FIRST_NAME_TEXT_FIELD).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.get_page_element(*RegisterPageLocators.LAST_NAME_TEXT_FIELD).send_keys(last_name)

    def fill_email(self, email):
        self.get_page_element(*RegisterPageLocators.EMAIL_TEXT_FIELD).send_keys(email)

    def fill_password(self, password):
        self.get_page_element(*RegisterPageLocators.PASSWORD_TEXT_FIELD).send_keys(password)

    def fill_confirm_password(self, password):
        self.get_page_element(*RegisterPageLocators.CONFIRM_PASSWORD_TEXT_FIELD).send_keys(password)

    def click_register_button(self):
        self.get_page_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    def register_new_user(self, first_name, last_name, email, password):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_confirm_password(password)
        self.click_register_button()
