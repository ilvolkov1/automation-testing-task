from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.category_page import CategoryPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from testdata import TestUser
import time
import pytest


def log_in(browser):
    link = LoginPage.login_page_link
    email = TestUser.email
    password = TestUser.password
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.log_in(email, password)
    return login_page


def add_to_cart(browser):
    link = ProductPage.product_page_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_to_cart()
    return product_page


@pytest.mark.smoke
class TestUserCanAddToBasketAndClearBasket:

    def test_user_can_add_product_to_cart_from_product_page(self, browser):
        log_in(browser)
        product_page = add_to_cart(browser)
        product_page.should_be_success_message()

    def test_user_can_clear_cart(self, browser):
        log_in(browser)

        link = CartPage.cart_page_link
        cart_page = CartPage(browser, link)
        cart_page.open()
        cart_page.should_be_cart_page()
        cart_page.clear_cart()
        cart_page.should_be_empty_cart()

    def test_user_can_add_product_to_cart_from_category_page(self, browser):
        log_in(browser)

        link = CategoryPage.category_page_link
        category_page = CategoryPage(browser, link)
        category_page.open()
        category_page.should_be_category_page()
        category_page.add_to_cart()
        category_page.should_be_success_message()


def test_user_can_update_cart(browser):
    log_in(browser)
    add_to_cart(browser)
    link = CartPage.cart_page_link
    cart_page = CartPage(browser, link)
    cart_page.open()
    cart_page.should_be_changed_total_cart_value()


@pytest.mark.smoke
def test_user_can_make_order(browser):
    log_in(browser)
    add_to_cart(browser)
    link = CartPage.cart_page_link
    cart_page = CartPage(browser, link)
    cart_page.open()
    cart_page.check_terms_of_service_checkbox()
    cart_page.click_checkout_button()
    order_page = OrderPage(browser, OrderPage.order_page_link)
    order_page.fill_billing_address_form(TestUser.first_name, TestUser.last_name, TestUser.email)
    order_page.click_billing_address_continue_button()
    order_page.click_shipping_address_continue_button()
    order_page.click_shipping_method_continue_button()
    order_page.click_payment_method_continue_button()
    order_page.click_payment_information_continue_button()
    order_page.click_confirm_order_button()
    order_page.should_be_success_message()
