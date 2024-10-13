from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install()) # verificar a versão do chrome e atualiza o webdriver

navegador = webdriver.Chrome(service = servico)

navegador.get('https://media-alunos17.netlify.app/')

nome = navegador.find_element(By.XPATH, "/html/body/app-root/app-formulario-escolar/form/input[1]")
nota1 = navegador.find_element(By.XPATH, "/html/body/app-root/app-formulario-escolar/form/input[2]")
nota2 = navegador.find_element(By.XPATH, "/html/body/app-root/app-formulario-escolar/form/input[3]")
enviar = navegador.find_element(By.XPATH, "/html/body/app-root/app-formulario-escolar/form/input[4]")

nome.clear()
nota1.clear()
nota2.clear()

nome.send_keys("André")
nota1.send_keys("10")
nota2.send_keys("7")
enviar.click()

time.sleep(5)