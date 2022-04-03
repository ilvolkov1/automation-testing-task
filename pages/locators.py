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


class ChangePasswordPageLocators:
    OLD_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#OldPassword")
    NEW_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#NewPassword")
    CONFIRM_NEW_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#ConfirmNewPassword")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".change-password-button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".result")
