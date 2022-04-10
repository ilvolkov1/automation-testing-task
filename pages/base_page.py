import selenium.common.exceptions
from .locators import BasePageLocators
import selenium


class BasePage:
    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_register_page(self):
        register_link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        register_link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except selenium.common.exceptions.NoSuchElementException:
            return False
        return True

    def get_page_element(self, how, what):
        element = self.browser.find_element(how, what)
        return element

    def get_page_element_attribute(self, how, what, attribute):
        element = self.browser.find_element(how, what)
        return element.get_attribute(attribute)

    def get_page_elements(self, how, what):
        elements = self.browser.find_elements(how, what)
        return elements
