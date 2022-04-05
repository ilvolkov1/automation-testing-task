from .base_page import BasePage
from .locators import CategoryPageLocators


class CategoryPage(BasePage):

    def should_be_category_page(self):
        self.should_be_category_page_form()

    def should_be_category_page_form(self):
        assert self.is_element_present(*CategoryPageLocators.CATEGORY_PAGE_FORM), "You are not in the Category page"

    def add_to_cart(self):
        self.get_page_element(*CategoryPageLocators.ADD_TO_CART_BUTTON).click()
