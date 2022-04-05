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
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, "updatecart")
    CART_TOTAL_VALUE = (By.CSS_SELECTOR, "order-total")


class ProductPageLocators:
    PRODUCT_DETAILS_FORM = (By.CSS_SELECTOR, "form#product-details-form")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".add-to-cart-button")
    PRODUCT_VALUE = (By.CSS_SELECTOR, ".product-price span")


class CategoryPageLocators:
    CATEGORY_PAGE_FORM = (By.CSS_SELECTOR, "category-page")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".buttons .product-box-add-to-cart-button")
