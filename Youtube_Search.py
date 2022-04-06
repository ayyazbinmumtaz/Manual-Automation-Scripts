from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "C:\Program Files\Python310\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("http://youtube.com")

time.sleep(3)

searchBox = driver.find_element_by_name('search_query')
searchBox.clear()
searchBox.send_keys('irfan junejo')

searchButton = driver.find_element_by_id("search-icon-legacy")
searchButton.click()
