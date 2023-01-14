from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url, "Login page is not open"
        print('test1 passed')

    def should_be_login_form(self):
        print('test2 passed')
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not available"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not available"
        print('test3 passed')