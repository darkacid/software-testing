import time

from selenium.webdriver import Chrome
from selenium import webdriver
import unittest

from pages import HomePage
from constants import *


class BaseTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()


class searchTest(BaseTest):
    def test_Valid_01(self):
        text_str = "mercedes գազ"
        home = HomePage(self.driver)
        home.input_search_text(text_str)
        search_res = home.complete_search()
        self.assertTrue(search_res.isResultFound())

    def test_Valid_02(self):
        text_str = "Mercedes"
        home = HomePage(self.driver)
        home.input_search_text(text_str)
        search_res = home.complete_search()
        text = search_res.get_result_text(text_str)
        self.assertIn(text_str,text)

    def test_Valid_03(self):
        text_str = "уроки"
        home = HomePage(self.driver)
        home.input_search_text(text_str)
        search_res = home.complete_search()
        text = search_res.get_result_text(text_str)
        self.assertIn(text_str,text)

    def test_Valid_04(self):
        text_str = "mErCeDes"
        home = HomePage(self.driver)
        home.input_search_text(text_str)
        search_res = home.complete_search()
        self.assertTrue(search_res.isResultFound())


    def test_InValid_01(self):
        text_str = "mercedes գ"
        home = HomePage(self.driver)
        home.input_search_text(text_str)
        search_res = home.complete_search()
        text = search_res.get_result_text(text_str)
        self.assertIn(text_str,text)

class AccountTest(BaseTest):


    def test_skip_email(self):
        #Should fail email not written
        home_page = HomePage(self.driver)
        account_page = home_page.click_account()
        register_page = account_page.click_register()
        register_page.enter_password("password01")
        register_page.enter_password_confirm("password01")
        register_page.clickPrivacyCheckbox()
        register_page.enter_captcha("4232")
        time.sleep(1)
        self.assertFalse(register_page.isRegisterAllowed())

    def test_passwordMismatch(self):
        #Should fail passwords don't match
        home_page = HomePage(self.driver)
        account_page = home_page.click_account()
        register_page = account_page.click_register()
        register_page.enter_email("valid@gmail.com")
        register_page.enter_password("password01")
        register_page.enter_password_confirm("password02")
        register_page.clickPrivacyCheckbox()
        register_page.enter_captcha("4232")
        time.sleep(1)
        self.assertFalse(register_page.isRegisterAllowed())

    def test_invalidEmail(self):
        # Should fail, email invalid
        home_page = HomePage(self.driver)
        account_page = home_page.click_account()
        register_page = account_page.click_register()
        register_page.enter_email("123")
        register_page.enter_password("password01")
        register_page.enter_password_confirm("password01")
        register_page.clickPrivacyCheckbox()
        register_page.enter_captcha("4232")
        time.sleep(1)
        self.assertFalse(register_page.isRegisterAllowed())

    def test_privacyCheckboxNotClicked(self):
        # Should fail, privacy checkbox not clicked
        home_page = HomePage(self.driver)
        account_page = home_page.click_account()
        register_page = account_page.click_register()
        register_page.enter_email("123")
        register_page.enter_password("password01")
        register_page.enter_password_confirm("password01")
        register_page.enter_captcha("4232")
        # register_page.clickPrivacyCheckbox()
        time.sleep(1)
        self.assertFalse(register_page.isRegisterAllowed())

    def test_validRegister(self):
        home_page = HomePage(self.driver)
        account_page = home_page.click_account()
        register_page = account_page.click_register()
        register_page.enter_email("123")
        register_page.enter_password("password01")
        register_page.enter_password_confirm("password01")
        register_page.enter_captcha("4232")
        register_page.clickPrivacyCheckbox()
        time.sleep(1)
        self.assertTrue(register_page.isRegisterAllowed())


if __name__ == '__main__':
    unittest.main()

