from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install()) # verificar a versão do chrome e atualiza o webdriver

navegador = webdriver.Chrome(service = servico)

input()