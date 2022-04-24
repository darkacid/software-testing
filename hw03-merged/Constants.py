from selenium.webdriver.common.by import By

class HomePageLocator:
    searchField = [By.ID,"idSearchBox"]
    searchResult = [By.XPATH,"//div[contains(text(),'{}')]"]

class VehicleLocators:
    adcheckbox = [By.XPATH,"//input[@id='idpo']"]
    priceStart = [By.XPATH,"//input[@id='idprice1']"]
    priceEnd = [By.XPATH, "//input[@id='idprice2']"]
    priceBtn = [By.XPATH,"//body/div[@id='main']/div[@id='pagecol']/div[@id='menul']/div[1]/form[1]/div[3]/div[1]/div[2]/a[1]"]

