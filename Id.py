from selenium import webdriver
import time

from selenium.webdriver.common import by

controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe") #esto es para poder ejecutar el driver e indicarle la ruta de donde esta
controlador.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2Fresponse_type=html") #get lo que me permite es darle el link de la pagina a testear
time.sleep(1)

#usuario = controlador.find_element_by_id("email--1")#le digo que busque elementos mediante el atributo de id en la pagina
usuario = webdriver.find_element(by.id, "email--1")
time.sleep(1)

clave = controlador.find_element_by_id("id_password")

usuario.send_keys("calavera_rip@outlook.com")#le ingreso valores a los script de arriba
time.sleep(5)
clave.send_keys("losBKrifanputas")

boton = controlador.find_element_by_id("submit-id-submit")
boton.click()

controlador.quit()