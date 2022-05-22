from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from constants import *



class BasePage:

    def __init__(self, driver):
        self.driver = driver
    def type_text(self,By,text):
        self.driver.find_element(*By).send_keys(text)
    def clear_field(self,By):
        self.driver.find_element(*By).clear()
    def get_text(self,By):
        return self.driver.find_element(*By).text
    def click(self,By):
        self.driver.find_element(*By).click()


class HomePage(BasePage):

    def input_search_text(self,text):
        self.type_text(search_field,text)

    def complete_search(self):
        self.type_text(search_field, Keys.RETURN)
        return SearchPage(self.driver)

    def click_account(self):
        self.click(account_link)
        return AccountPage(self.driver)

class SearchPage(BasePage):

    def get_result_text(self,text):
        search_locator = [searchResult[0],searchResult[1].format(text)]
        return self.get_text(search_locator)
    def isResultFound(self):
        try:
            self.driver.find_element(searchNonExistent)
            return False
        except:
            return True


class AccountPage(BasePage):
    def click_register(self):
        self.click(register_link)
        return RegisterPage(self.driver)

class RegisterPage(BasePage):

    def clickPrivacyCheckbox(self):
        self.click(confirm_checkbox)
    def enter_email(self,text):
        self.type_text(email,text)
    def enter_password(self,text):
        self.type_text(password,text)
    def enter_password_confirm(self,text):
        self.type_text(password_confirm,text)
    def enter_captcha(self,text):
        self.type_text(captchaField, text)

    def isRegisterAllowed(self):
        # True if allowed, False otherwise
        try:
            self.driver.find_element(*submit_button_not_allowed) #Element is found if button is greyed out
            return False
        except:
            return True