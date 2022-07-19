#Testing por classname
from selenium import webdriver

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.get("https://www.udemy.com/join/login-popup/?skip_suggest=1&locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2Fresponse_type=html")

user = driver.find_element_by_class_name("form-control")
clave = driver.find_element_by_class_name("textinput textInput form-control")

user.send_keys("calavera_rip@outlook.com")
clave.send_keys("losBKrifanputas")

boton = driver.find_element_by_class_name("btn btn-primary")
boton.click()

driver.close()