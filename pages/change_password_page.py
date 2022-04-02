from .base_page import BasePage
from .locators import ChangePasswordPageLocators


class ChangePasswordPage(BasePage):
    change_password_link = "http://demowebshop.tricentis.com/customer/changepassword"

    def should_be_change_password_page(self):
        self.should_be_change_password_url()
        self.should_be_change_password_form()

    def should_be_change_password_url(self):
        assert "changepassword" in self.url, "This is not Change Password Page"

    def should_be_change_password_form(self):
        assert self.is_element_present(*ChangePasswordPageLocators.OLD_PASSWORD_TEXT_FIELD), "Can't find old password text field"
        assert self.is_element_present(*ChangePasswordPageLocators.NEW_PASSWORD_TEXT_FIELD), "Can't find new password text field"
        assert self.is_element_present(*ChangePasswordPageLocators.CONFIRM_NEW_PASSWORD_TEXT_FIELD), "Can't find confirm new password text field"

    def should_be_success_message(self):
        assert "Password was changed" in self.get_page_element(*ChangePasswordPageLocators.SUCCESS_MESSAGE).text, "No success message"

    def fill_old_password(self, old_password):
        self.get_page_element(*ChangePasswordPageLocators.OLD_PASSWORD_TEXT_FIELD).send_keys(old_password)

    def fill_new_password(self, new_password):
        self.get_page_element(*ChangePasswordPageLocators.NEW_PASSWORD_TEXT_FIELD).send_keys(new_password)

    def fill_new_password_confirmation(self, new_password):
        self.get_page_element(*ChangePasswordPageLocators.NEW_PASSWORD_TEXT_FIELD).send_keys(new_password)

    def click_button_change_password(self):
        self.get_page_element(*ChangePasswordPageLocators.CHANGE_PASSWORD_BUTTON).click()

    def change_password(self, old_password, new_password):
        self.fill_old_password(old_password)
        self.fill_new_password(new_password)
        self.fill_new_password_confirmation(new_password)
        self.click_button_change_password()
