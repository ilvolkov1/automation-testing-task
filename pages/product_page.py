from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_page_link = "http://demowebshop.tricentis.com/health"

    def should_be_product_page(self):
        self.should_be_product_details_form()

    def should_be_product_details_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DETAILS_FORM), "You are not in the Product page"

    def add_to_cart(self):
        self.get_page_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def get_product_value(self):
        return self.get_page_element(*ProductPageLocators.PRODUCT_VALUE).text

    def should_be_success_message(self):
        assert "The product has been added to your shopping cart" in self.get_page_element(*ProductPageLocators.SUCCESS_MESSAGE_ADDED_TO_CART).text, "You did not added item to the cart"
