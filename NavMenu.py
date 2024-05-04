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

elementos_a = navegador.find_elements(By.CSS_SELECTOR, ".menu-horizontal a")

for elemento_a in elementos_a:
    url_link = elemento_a.get_attribute("href")
    navegador.execute_script("window.open('{}', '_blank');".format(url_link))
    time.sleep(2)

navegador.quit() 
# O código navega até o site da Apotiguar, seleciona a região 'Grande São Luís', aceita os cookies, abre cada link de elemento 'a' em uma nova aba e aguarda 2 segundos em cada aba antes de fechar o navegador.