from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators, ConfirmEmailPageLocators
from locators.login_page_locators import LoginPageLocators
from utilities.data import random_email, random_password


class RegisterPage(BasePage):
    def select_role_seller(self):
        self.browser.find_element(*RegisterPageLocators.SELECT_ROLE_SELLER).click()

    def select_role_supplier(self):
        self.browser.find_element(*RegisterPageLocators.SELECT_ROLE_SUPPLIER).click()

    def enter_email_random(self):
        self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL).send_keys(random_email)

    def enter_email(self, email):
        self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL).send_keys(email)

    def enter_password(self):
        self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD).send_keys(random_password)

    def submit_create_account(self):
        self.browser.find_element(*RegisterPageLocators.CREATE_ACCOUNT_BTN).submit()

    def complete_user_registration(self):
        self.browser.find_element(*ConfirmEmailPageLocators.CONFIRM_EMAIL_LOGIN_LINK).click()

    def enter_register_email(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(random_email)

    def enter_register_password(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(random_password)

    def submit_login(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).submit()

    # def enter_invalid_email(self):
    #     self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(INVALID_EMAIL)
    #     self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).click()
    #
    # def enter_invalid_password(self):
    #     self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(INVALID_PASSWORD)
    #     self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).click()

    # def enter_email(self, email):
    #     self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL).send_keys(email)
