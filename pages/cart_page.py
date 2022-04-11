from .base_page import BasePage
from .locators import CartPageLocators
import time


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

    def clear_cart(self):
        elements = self.get_page_elements(*CartPageLocators.REMOVE_FROM_CART_CHECKBOX)
        if len(elements) != 0:
            for element in elements:
                element.click()
            self.get_page_element(*CartPageLocators.UPDATE_CART_BUTTON).click()

    def should_be_empty_cart(self):
        assert "Your Shopping Cart is empty!" in self.get_page_element(*CartPageLocators.SUMMARY_CONTENT_CART_MESSAGE).text, "Cart is not empty"

    def increase_quantity_by_one(self):
        num = int(self.get_page_element_attribute(*CartPageLocators.QUANTITY_TEXT_FIELD, "value"))
        self.get_page_element(*CartPageLocators.QUANTITY_TEXT_FIELD).clear()
        self.get_page_element(*CartPageLocators.QUANTITY_TEXT_FIELD).send_keys(num+1)

    def should_be_changed_total_cart_value(self):
        total_cart_value = float(self.get_total_cart_value())
        price = float(self.get_price())
        self.increase_quantity_by_one()
        self.update_shopping_cart()
        assert float(self.get_total_cart_value()) == total_cart_value+price, "total value didn't changed"

    def get_price(self):
        return self.get_page_element(*CartPageLocators.PRODUCT_UNIT_PRICE).text

    def check_terms_of_service_checkbox(self):
        self.get_page_element(*CartPageLocators.AGREEMENT_CHECKBOX).click()

    def click_checkout_button(self):
        self.get_page_element(*CartPageLocators.CHECKOUT_BUTTON).click()

