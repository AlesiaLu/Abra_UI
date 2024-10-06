from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):
    def enter_email(self, email):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)

    def enter_password(self, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)

    def enter_invalid_email(self, email):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).click()

    def enter_invalid_password(self, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).click()

    def submit_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).submit()

    def go_to_empty_login_data(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys('')
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys('')
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).click()

    def go_to_password_visibility(self):
        self.browser.find_element(*LoginPageLocators.PASSWORD_VISIBILITY).click()

    def go_to_forgot_password(self):
        self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_BTN).click()

    def find_profile(self):
        profile = self.browser.find_element(*MainPageLocators.PROFILE_BTN)
        return profile
