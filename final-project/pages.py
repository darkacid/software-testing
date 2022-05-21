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
    def click_my_account(self):
        self.click(account_link)
        return RegisterPage(self.driver)

class RegisterPage(BasePage):
    def clickEmail(self):
        pass

    def clickPassword(self):
        pass

    def clickPasswordConfirm(self):
        pass

    def enter_email(self):
        pass