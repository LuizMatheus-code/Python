from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://google.com/")

location = browser.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')

location.send_keys("Login")

location.send_keys(Keys.ENTER)

sleep(2)