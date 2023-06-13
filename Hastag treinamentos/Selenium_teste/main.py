from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=servico)

browser.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium")
