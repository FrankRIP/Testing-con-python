from selenium import webdriver
import time
controlador = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")


controlador.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2Fresponse_type=html")
usuario = controlador.find_element_by_name("email")
clave = controlador.find_element_by_name("password")

usuario.send_keys("calavera_rip@outlook.com")
clave.send_keys("losBKrifanputas")

boton = controlador.find_element_by_name("submit")
boton.click()

controlador.quit()