from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.hashtagtreinamentos.com/")
    
    page.locator('xpath=/html/body/div[1]/div[9]/div/div/form/div[1]/input').click()
    page.fill('xpath=/html/body/div[1]/div[9]/div/div/form/div[1]/input', "nome")
    
    time.sleep(1)

    page.locator('xpath=/html/body/div[1]/div[9]/div/div/form/div[2]/input').click()
    page.fill('xpath=/html/body/div[1]/div[9]/div/div/form/div[2]/input', "email")

    time.sleep(1)

    page.locator('xpath=/html/body/div[1]/div[1]/div/div/div[1]/a[1]').click()

    time.sleep(2)
