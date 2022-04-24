from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = Chrome()
url = "https://www.estate.am/%D5%BE%D5%A1%D6%80%D5%B1%D5%B8%D5%BE-%D5%A2%D5%B6%D5%A1%D5%AF%D5%A1%D6%80%D5%A1%D5%B6%D5%B6%D5%A5%D6%80-%D5%A5%D6%80%D6%87%D5%A1%D5%B6%D5%B8%D6%82%D5%B4-s13864"
driver.get(url)

time.sleep(2)
#Change sorting order
Select(driver.find_element(By.ID,value="list-sort")).select_by_visible_text("գնի")
time.sleep(2)

#Main apartment list
apartments = driver.find_elements(by=By.CLASS_NAME, value="item.cfix")

for apartment in apartments:
    title = apartment.find_element(by=By.CSS_SELECTOR,value="h2").text
    text = apartment.find_element(by=By.CSS_SELECTOR,value="p").text
    num_hits = apartment.find_element(by=By.XPATH, value=".//span[@class='hits']").text
    print(title)
    print(text)
    print(num_hits)

time.sleep(2)
#Click on page 2
next_page = driver.find_element(by=By.CSS_SELECTOR, value="a[href*='?page=2']")
next_page.click()