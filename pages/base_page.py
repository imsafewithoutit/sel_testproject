from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)
    
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()
    
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
    
    # проверка, что элемент не появляется на странице в течение заданного времени. 
    # Тест упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        
        return False

    # проверка, что какой-то элемент исчезает (явное ожидание). 
    # Будет ждать, пока элемент не исчезнет.
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        
        return True
