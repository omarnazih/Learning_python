from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#chrome webdriver path
PATH = "C:\Program Files (x86)\chromedriver.exe"     
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net/")
print(driver.title)


search = driver.find_element_by_name("s")
search.send_keys("Test")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(5)
	
driver.close()