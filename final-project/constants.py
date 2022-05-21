from selenium.webdriver.common.by import By

search_field = [By.ID, "idSearchBox"]
searchResult = [By.XPATH,"//div[contains(text(),'{}')]"] #Get first result, no better locator available
searchNonExistent = [By.CLASS_NAME,".notfound"]

BASE_URL = "https://list.am/am"