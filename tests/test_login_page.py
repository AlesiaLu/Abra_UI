import pytest
import requests as requests
import time
import db_queries
import settings
from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from settings import Urls, Config
import allure
from allure_commons.types import AttachmentType


@allure.title("Test Authentication")
@allure.feature('user_login')
@allure.story('Enter valid email and password')
@allure.severity('blocker')
@pytest.mark.smoke
def test_login_with_valid_data(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.enter_email(settings.Config.VALID_EMAIL_SELLER)
    page.enter_password(settings.Config.VALID_PASSWORD)
    page.submit_login()
    with allure.step('Make screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='result8', attachment_type=AttachmentType.PNG)
    profile_btn = page.find_profile()
    assert f"'{profile_btn}' is present"

    response = requests.get(Urls.BASE_URL)
    assert response.status_code == 200, f"{response.status_code} is not our expectation"
    assert page.find_profile()
    assert len(db_queries.get_user_by_email(Config.VALID_EMAIL_SELLER)) > 0


def test_login_with_invalid_password(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.enter_email(settings.Config.VALID_EMAIL_SELLER)
    page.enter_invalid_password(settings.Config.INVALID_PASSWORD)
    time.sleep(2)
    error_invalid_password = browser.find_element(*LoginPageLocators.INVALID_PASSWORD)
    assert error_invalid_password.text == 'Invalid password', (f" '{error_invalid_password.text}' is not expected text "
                                                               f"of error")
    assert browser.find_element(*LoginPageLocators.LOGIN_BTN).get_attribute("disabled") is not None


def test_login_with_empty_data(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.go_to_empty_login_data()
    error_email_is_required = browser.find_element(*LoginPageLocators.EMAIL_IS_REQUIRED)
    assert error_email_is_required.text == 'Email is required', (f" '{error_email_is_required.text}' is not expected "
                                                                 f"text of error")
    error_password_is_required = browser.find_element(*LoginPageLocators.PASSWORD_IS_REQUIRED)
    assert error_password_is_required.text == 'Password is required', (f" '{error_password_is_required.text}' is not "
                                                                       f"expected text of error")
    assert browser.find_element(*LoginPageLocators.LOGIN_BTN).get_attribute("disabled") is not None


def test_login_visible_password(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.enter_email(settings.Config.VALID_EMAIL_SELLER)
    page.enter_password(settings.Config.VALID_PASSWORD)
    password_visibility = browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
    assert password_visibility.get_attribute("type") == "password"
    page.go_to_password_visibility()
    assert password_visibility.get_attribute("type") == "text"


def test_login_with_invalid_email(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.enter_invalid_email(settings.Config.INVALID_EMAIL)
    error_invalid_email = browser.find_element(*LoginPageLocators.INVALID_EMAIL)
    assert error_invalid_email.text == 'Invalid email', f" '{error_invalid_email.text}' is not expected text of error"
    assert browser.find_element(*LoginPageLocators.LOGIN_BTN).get_attribute("disabled") is not None


def test_forgot_password(browser):
    page = LoginPage(browser, Urls.LOGIN_URL)
    page.open()
    page.go_to_forgot_password()
