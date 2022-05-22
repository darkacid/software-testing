from selenium.webdriver.common.by import By

search_field = [By.ID, "idSearchBox"]
searchResult = [By.XPATH,"//div[contains(text(),'{}')]"] #Get first result, no better locator available
searchNonExistent = [By.CLASS_NAME,".notfound"]


account_link = [By.ID,"ma"]
register_link = [By.CLASS_NAME,"bblink"]
email = [By.XPATH," //input[@id='_idyour_email']"]
password = [By.XPATH,"//input[@id='_idpassword']"]
password_confirm = [By.XPATH,"//input[@id='_idconfirm_password']"]
confirm_checkbox = [By.XPATH,"//input[@id='_idagree']"]
captchaField = [By.XPATH,"//input[@id='_idverification_number']"]
submit_button_not_allowed = [By.XPATH," //input[@id='action__form_action0' and @class='sub']"]
BASE_URL = "https://list.am/am"