from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import OrderPageLocators
import time
from selenium.webdriver.support.ui import Select
import random


class OrderPage(BasePage):
    order_page_link = "http://demowebshop.tricentis.com/onepagecheckout"

    def select_new_address_from_dropdown(self):
        try:
            select = Select(self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_DROPDOWN))
            select.select_by_visible_text("New Address")
        except NoSuchElementException:
            print("This is your first order")

    def fill_billing_address_form(self, first_name, last_name, email):
        self.select_new_address_from_dropdown()
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.select_country()
        self.fill_city()
        self.fill_address()
        self.fill_zip_code()
        self.fill_phone_number()

    def fill_first_name(self, first_name):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_FIRST_NAME).clear()
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_LAST_NAME).clear()
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_LAST_NAME).send_keys(last_name)

    def fill_email(self, email):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_EMAIL).clear()
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_EMAIL).send_keys(email)

    def select_country(self):
        try:
            select = Select(self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_COUNTRY_DROPDOWN))
            select.select_by_value(str(random.randint(1, 50)))
        except NoSuchElementException:
            print("This is your first orderasfsdfbhds")

    def fill_city(self):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_CITY).send_keys(random.randint(1, 20000))

    def fill_address(self):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_ADDRESS).send_keys(random.randint(1, 20000))

    def fill_zip_code(self):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_ZIP_CODE).send_keys(random.randint(1, 20000))

    def fill_phone_number(self):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_PHONE_NUMBER).send_keys(random.randint(1, 20000))

    def click_billing_address_continue_button(self):
        self.get_page_element(*OrderPageLocators.BILLING_ADDRESS_CONTINUE).click()

    def click_shipping_address_continue_button(self):
        self.get_page_element(*OrderPageLocators.SHIPPING_ADDRESS_CONTINUE).click()

    def click_shipping_method_continue_button(self):
        self.get_page_element(*OrderPageLocators.SHIPPING_METHOD_CONTINUE).click()

    def click_payment_method_continue_button(self):
        self.get_page_element(*OrderPageLocators.PAYMENT_METHOD_CONTINUE).click()

    def click_payment_information_continue_button(self):
        self.get_page_element(*OrderPageLocators.PAYMENT_INFORMATION_CONTINUE).click()

    def click_confirm_order_button(self):
        self.get_page_element(*OrderPageLocators.CONFIRM_ORDER_BUTTON).click()

    def should_be_success_message(self):
        assert "Your order has been successfully processed!" in self.get_page_element(*OrderPageLocators.SUCCESS_MESSAGE).text, "Order is not completed"
