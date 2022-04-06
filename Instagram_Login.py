from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH= "C:\Program Files\Python310\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://instagram.com')

searchBox_uname = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
searchBox_uname.send_keys("Username")

time.sleep(3)

searchBox_pwd = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
searchBox_pwd.send_keys("Password")

time.sleep(3)

searchButton = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
searchButton.click()

time.sleep(10)

driver.close()
