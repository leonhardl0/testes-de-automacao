from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scroll_page(driver, pixels):
    driver.execute_script("window.scrollBy(0, {})".format(pixels))

navegador = webdriver.Chrome()
navegador.get("https://www.apotiguar.com.br/")

elemento_1 = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Selecione')]")))
elemento_1.click()

elemento_2 = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Grande São Luís')]")))
elemento_2.click()

time.sleep(2)

botao_cookies = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "cookie-btn")))
botao_cookies.click()

campo_busca = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "txtBuscaMobile")))
campo_busca.send_keys("Cadeira de Balanço")

botao_busca = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "isearch")))
botao_busca.click()

time.sleep(2)

scroll_page(navegador, 400)

time.sleep(2)

navegador.quit()  
# O código navega até o site da Apotiguar, seleciona a região 'Grande São Luís', aceita os cookies, preenche o campo de busca com "Cadeira de Balanço", clica no botão de busca, rola a página e aguarda antes de fechar o navegador.