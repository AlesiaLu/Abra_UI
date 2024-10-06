from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def go_to_profile(self):
        profile_btn = self.browser.find_element(*MainPageLocators.PROFILE_BTN)
        profile_btn.click()

