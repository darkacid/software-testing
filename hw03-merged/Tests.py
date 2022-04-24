from selenium.webdriver import Chrome
import unittest

from Pages import Homepage,VehiclePage
import time
class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = Chrome()
    def tearDown(self):
        self.driver.quit()
    def screenshot(self):
        self.driver.save_screenshot(self.id()+".png")


class VehicleTest(BaseTest):
    def testAdsButton(self):
        vehicle = VehiclePage(self.driver)
        vehicle.toggleAds()

    def testSetPrice(self):
        vehicle = VehiclePage(self.driver)
        vehicle.setPriceRange(2000,15000)

class SearchTest(BaseTest):
    def testSearch(self):
        home = Homepage(self.driver)
        result = home.search("Mercedes")
        print("Search result: ",result)
        self.screenshot()
        self.assertIn("Mercedes",result)


if __name__ == '__main__':
    unittest.main()

