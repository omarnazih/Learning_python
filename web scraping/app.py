from selenium import webdriver

#chrome webdriver path
PATH = "C:\Program Files (x86)\chromedriver.exe"     

driver = webdriver.Chrome(PATH)

driver.get("https://9xbuddy.org/")
driver.close()