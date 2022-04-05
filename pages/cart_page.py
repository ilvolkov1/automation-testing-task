from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    cart_page_link = "http://demowebshop.tricentis.com/cart"

    def should_be_cart_page(self):
        self.should_be_cart_url()
        self.should_be_cart_header()

    def should_be_cart_url(self):
        assert "cart" in self.url, "This is not Cart Page"

    def should_be_cart_header(self):
        assert "Shopping cart" in self.get_page_element(*CartPageLocators.CART_HEADER).text, "You are not in the Cart page"

    def update_shopping_cart(self):
        self.get_page_element(*CartPageLocators.UPDATE_CART_BUTTON).click()

    def get_total_cart_value(self):
        return self.get_page_element(*CartPageLocators.CART_TOTAL_VALUE).text
