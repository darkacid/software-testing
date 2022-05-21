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
        text = search_res.get_result_text(text_str)
        self.assertIn(text_str,text)

    def test_Valid_02(self):
        text_str = "Mercedes"
        home = HomePage(self.driver)
        home.input_search_text(text_str)
        search_res = home.complete_search()
        text = search_res.get_result_text(text_str)
        self.assertIn(text_str,text)