from .base_page import BasePage
from .locators import CategoryPageLocators


class CategoryPage(BasePage):
    category_page_link = "http://demowebshop.tricentis.com/books"

    def should_be_category_page(self):
        self.should_be_category_page_form()

    def should_be_category_page_form(self):
        assert self.is_element_present(*CategoryPageLocators.CATEGORY_PAGE_FORM), "You are not in the Category page"

    def add_to_cart(self):
        self.get_page_element(*CategoryPageLocators.ADD_TO_CART_BUTTON).click()
        self.should_be_success_message()

    def should_be_success_message(self):
        assert "The product has been added to your shopping cart" in self.get_page_element(*CategoryPageLocators.SUCCESS_MESSAGE_ADDED_TO_CART).text, "You did not added item to the cart"
