from .base_page import BasePage
from .locators import OrderPageLocators
import time


class OrderPage(BasePage):
    order_page_link = "http://demowebshop.tricentis.com/onepagecheckout"