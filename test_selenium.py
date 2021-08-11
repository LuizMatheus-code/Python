from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://ri.magazineluiza.com.br/")
browser.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/p').click()
browser.find_element_by_xpath('//*[@id="Form1"]/div[15]/div[3]/div/div/div[1]/ul/li[2]/a').click()
