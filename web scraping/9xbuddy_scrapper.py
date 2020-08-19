from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#chrome webdriver path
PATH = "C:\Program Files (x86)\chromedriver.exe"     
driver = webdriver.Chrome(PATH)

driver.get("https://9xbuddy.org/")
print(driver.title)


search = driver.find_element_by_class_name("mr-4")
search.send_keys("https://www.youtube.com/watch?v=92wtDKCtOiU")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(20)

driver.quit()
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    
    articles = driver.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()

	
