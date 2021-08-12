from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://ri.magazineluiza.com.br/")
browser.find_element_by_xpath('//*[@id="Form1"]/div[8]/div/div[2]/div/input').send_keys('Magazine Luiza')
browser.find_element_by_xpath('//*[@id="Form1"]/div[8]/div/div[2]/div/span').click()
