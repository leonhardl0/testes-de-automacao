from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

navegador = webdriver.Chrome()
navegador.get("https://www.apotiguar.com.br/")

elemento_1 = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Selecione')]")))
elemento_1.click()

elemento_2 = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Grande São Luís')]")))
elemento_2.click()

time.sleep(2)

botao_cookies = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "cookie-btn")))
botao_cookies.click()

time.sleep(2)

navegador.quit()  
# O código navega até o site da Apotiguar, seleciona a região 'Grande São Luís', aceita os cookies e fecha o navegador.