from selenium.webdriver.common.by import By


class RegisterPageLocators:
    SELECT_ROLE_SELLER = (By.XPATH, '//button[contains(text(), "here to buy")]')
    SELECT_ROLE_SUPPLIER = (By.XPATH, '//button[contains(text(), "here to sell")]')
    REGISTER_EMAIL = (By.XPATH, '//input[@class="Input_input__YeDuE"][@name="email"]')
    REGISTER_PASSWORD = (By.XPATH, '//input[@class="Input_input__YeDuE"][@name="password"]')
    CREATE_ACCOUNT_BTN = (By.XPATH, '//button[@type="submit"]')
    EXISTING_EMAIL = (By.CLASS_NAME, 'NoticePopup_message__Thz3M')
    INVALID_EMAIL = (By.XPATH, '//span[text()="Invalid email"]')
    INVALID_PASSWORD = (By.XPATH, '//span[text()="Invalid password"]')


class ConfirmEmailPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, ".ContentMessage_header__Vwy9L")
    TEXT_EMAIL_CONFIRMED = (By.CLASS_NAME, 'ContentMessage_header__Vwy9L')
    CONFIRM_EMAIL_LOGIN_LINK = (By.CLASS_NAME, 'ConfirmEmailPage_link__kO5Ku')


# class SetupAccountPage:
