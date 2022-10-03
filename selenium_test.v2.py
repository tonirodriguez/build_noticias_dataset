import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.laie.es")

cookies = driver.find_element(by=By.ID,value="onetrust-accept-btn-handler")
cookies.send_keys(Keys.ENTER)

info = driver.find_element(by=By.CLASS_NAME,value="HomeSlider-moreInfoBtn")
info.send_keys(Keys.ENTER)

time.sleep(10)

driver.close()