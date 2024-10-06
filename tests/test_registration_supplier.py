import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import db_queries
from locators.main_page_locators import MainPageLocators
from locators.register_page_locators import RegisterPageLocators, ConfirmEmailPageLocators
from pages.register_page import RegisterPage
from settings import Urls, Config
from utilities.data import random_email
from utilities.temp_mail import get_confirmation_link


@pytest.mark.smoke
def test_register_supplier_with_valid_data(browser):
    page = RegisterPage(browser, Urls.REGISTER_URL)
    page.open()
    page.select_role_supplier()
    page.enter_email_random()
    page.enter_password()
    page.submit_create_account()

    # Ожидание уведомления об отправке письма
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            ConfirmEmailPageLocators.LOGIN_LINK,
            "A link for sign up has been sent to your email address."))
    print("Регистрация прошла успешно, ожидаем письмо для подтверждения.")

    # Ожидание получения письма
    time.sleep(5)

    # Получаем confirmation_link через функцию
    confirmation_link = get_confirmation_link(browser)

    # Переход по ссылке для подтверждения регистрации
    browser.get(confirmation_link)

    # Ожидание успешного подтверждения
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            ConfirmEmailPageLocators.TEXT_EMAIL_CONFIRMED,
            "Email confirmed."))
    print("Регистрация успешно подтверждена!")
    page.complete_user_registration()
    page.enter_register_email()
    page.enter_register_password()
    page.submit_login()
    time.sleep(1000)
