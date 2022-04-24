from Constants import *

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class BasePage():
    def __init__(self, driver):
        self.driver = driver



class Homepage(BasePage):
    def __init__(self,driver):
        self.locator = HomePageLocator
        self.url = "https://www.list.am/en/"
        super().__init__(driver)
    def search(self,string):
        self.driver.get(self.url)
        self.driver.find_element(*self.locator.searchField).send_keys(string,Keys.RETURN)
        result = self.driver.find_element(self.locator.searchResult[0],self.locator.searchResult[1].format(string))
        return result.text



class VehiclePage(BasePage):
    def __init__(self,driver):

        self.url = "https://www.list.am/category/16"
        self.locator = VehicleLocators


        super().__init__(driver)
        self.driver.get(self.url)


    def toggleAds(self):
        self.driver.find_element(*self.locator.adcheckbox).click()
    def setPriceRange(self,start:int,end:int):
        self.driver.find_element(*self.locator.priceStart).send_keys(start)
        self.driver.find_element(*self.locator.priceEnd).send_keys(end)
        self.driver.find_element(*self.locator.priceBtn).click()