from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "/login")
    REGISTER_LINK = (By.CSS_SELECTOR, "/register")
    BASKET_BUTTON = (By.CSS_SELECTOR, "/cart")


class RegisterPageLocators():
    FIRST_NAME_TEXT_FIELD = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME_TEXT_FIELD = (By.CSS_SELECTOR, "#LastName")
    EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, "#Email")
    PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#Password")
    CONFIRM_PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#ConfirmPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register-button")


class LoginPageLocators():
    EMAIL_TEXT_FIELD = (By.CSS_SELECTOR, "#Email")
    PASSWORD_TEXT_FIELD = (By.CSS_SELECTOR, "#Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")

class ChangePasswordPageLocators():
    pass
