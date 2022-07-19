from selenium import webdriver

driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
driver.maximize_windows() #esto es para maximiza la venta que va a abrir el chromedriver

driver.get("https://www.reddit.com/")#voy a obtener el link de donde quiero hacer el testing

driver.close()