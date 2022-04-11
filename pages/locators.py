from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "/login")
    REGISTER_LINK = (By.CSS_SELECTOR, "/register")
    BASKET_BUTTON = (By.CSS_SELECTOR, "/cart")
    LOGOUT_LINK = (By.CSS_SELECTOR, ".ico-logout")


class RegisterPageLocators:
    FIRST_NAME_TEXT_FIELD = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME_TEXT_FIELD = (By.CSS_SELECTOR, "#LastName")
    EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, "#Email")
    PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#ConfirmPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register-button")
    REGISTER_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".page-body .result")
    EXISTING_EMAIL_MESSAGE = (By.CSS_SELECTOR, ".message-error li")


class LoginPageLocators:
    EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, "#Email")
    PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    HEADER_EMAIL = (By.CSS_SELECTOR, ".header .account")
    INCORRECT_CREDENTIALS_MESSAGE = (By.CSS_SELECTOR, ".message-error li")


class ChangePasswordPageLocators:
    OLD_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#OldPassword")
    NEW_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#NewPassword")
    CONFIRM_NEW_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#ConfirmNewPassword")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".change-password-button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".result")
    OLD_PASSWORD_DOESNT_MATCH_MESSAGE = (By.CSS_SELECTOR, ".message-error li")


class CartPageLocators:
    CART_HEADER = (By.CSS_SELECTOR, "h1")
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, "input[name=updatecart]")
    CART_TOTAL_VALUE = (By.CSS_SELECTOR, ".product-price")
    REMOVE_FROM_CART_CHECKBOX = (By.CSS_SELECTOR, ".cart-item-row input[type=checkbox]")
    SUMMARY_CONTENT_CART_MESSAGE = (By.CSS_SELECTOR, ".order-summary-content")
    QUANTITY_TEXT_FIELD = (By.CSS_SELECTOR, ".qty-input")
    PRODUCT_UNIT_PRICE = (By.CSS_SELECTOR, ".product-unit-price")
    AGREEMENT_CHECKBOX = (By.CSS_SELECTOR, "div #termsofservice")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "div #checkout")


class ProductPageLocators:
    PRODUCT_DETAILS_FORM = (By.CSS_SELECTOR, "form#product-details-form")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCT_VALUE = (By.CSS_SELECTOR, ".product-price span")
    SUCCESS_MESSAGE_ADDED_TO_CART = (By.CSS_SELECTOR, "#bar-notification .content")


class CategoryPageLocators:
    CATEGORY_PAGE_FORM = (By.CSS_SELECTOR, ".category-page")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".buttons .product-box-add-to-cart-button")
    SUCCESS_MESSAGE_ADDED_TO_CART = (By.CSS_SELECTOR, "#bar-notification .content")


class OrderPageLocators:
    BILLING_ADDRESS_DROPDOWN = (By.CSS_SELECTOR, "div #billing-address-select")
    BILLING_ADDRESS_FIRST_NAME = (By.CSS_SELECTOR, "#BillingNewAddress_FirstName")
    BILLING_ADDRESS_LAST_NAME = (By.CSS_SELECTOR, "#BillingNewAddress_LastName")
    BILLING_ADDRESS_EMAIL = (By.CSS_SELECTOR, "#BillingNewAddress_Email")
    BILLING_ADDRESS_COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select#BillingNewAddress_CountryId")
    BILLING_ADDRESS_CITY = (By.CSS_SELECTOR, "#BillingNewAddress_City")
    BILLING_ADDRESS_ADDRESS = (By.CSS_SELECTOR, "#BillingNewAddress_Address1")
    BILLING_ADDRESS_ZIP_CODE = (By.CSS_SELECTOR, "#BillingNewAddress_ZipPostalCode")
    BILLING_ADDRESS_PHONE_NUMBER = (By.CSS_SELECTOR, "#BillingNewAddress_PhoneNumber")
    BILLING_ADDRESS_CONTINUE = (By.CSS_SELECTOR, ".button-1.new-address-next-step-button:nth-child(1)")
    SHIPPING_ADDRESS_CONTINUE = (By.CSS_SELECTOR, ".button-1.new-address-next-step-button:nth-child(2)")
    SHIPPING_METHOD_CONTINUE = (By.CSS_SELECTOR, ".button-1.shipping-method-next-step-button")
    PAYMENT_METHOD_CONTINUE = (By.CSS_SELECTOR, ".button-1.payment-method-next-step-button")
    PAYMENT_INFORMATION_CONTINUE = (By.CSS_SELECTOR, ".button-1.payment-info-next-step-button")
    CONFIRM_ORDER_BUTTON = (By.CSS_SELECTOR, ".button-1.confirm-order-next-step-button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".order-completed strong")