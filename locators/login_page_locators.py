from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.XPATH, '//input[@name="email"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@type="password"]')
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')
    INVALID_PASSWORD = (By.XPATH, '//span[text()= "Invalid password"]')
    INVALID_EMAIL = (By.XPATH, '//span[text()= "Invalid email"]')
    EMAIL_IS_REQUIRED = (By.XPATH, '//span[text()= "Email is required"]')
    PASSWORD_IS_REQUIRED = (By.XPATH, '//span[text()= "Password is required"]')
    PASSWORD_VISIBILITY = (By.XPATH, '//button[@class="ButtonIcon_button__QdSfh Input_button__Lhars"]')
    FORGOT_PASSWORD_BTN = (By.CSS_SELECTOR, 'a[href="/forgot_password"]')

