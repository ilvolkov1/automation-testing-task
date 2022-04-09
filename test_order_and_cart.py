from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.category_page import CategoryPage
from pages.login_page import LoginPage
from testdata import TestUser
import time
import pytest


class TestUserCanAddToBasket:
    def test_user_can_add_product_to_cart_from_product_page(self, browser):
        link = LoginPage.login_page_link
        email = TestUser.email
        password = TestUser.password
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.log_in(email, password)

        link = ProductPage.product_page_link
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_to_cart()
        product_page.should_be_success_message()

    def test_user_can_add_product_to_cart_from_category_page(self, browser):
        link = LoginPage.login_page_link
        email = TestUser.email
        password = TestUser.password
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.log_in(email, password)

        link = CategoryPage.category_page_link
        category_page = CategoryPage(browser, link)
        category_page.open()
        category_page.should_be_category_page()
        category_page.add_to_cart()
        category_page.should_be_success_message()
