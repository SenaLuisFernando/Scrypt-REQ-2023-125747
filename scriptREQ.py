import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#----------CONFIGURACION-----------------
#cambiar ruta de su chrome driver y el navegador que usen
#LINUX
#driver = webdriver.Chrome('/usr/bin/chromedriver')
#WINDOWS
#driver = webdriver.chrome('C:/Users/lusena/Documents/chromedriver-win64/chromedriver')
#CHROME DRIVE EN LINEA CON EDGE
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#url gsmarena
driver.get('http://www.gsmarena.com/');

#-------------CODIGO----------------
time.sleep(5)
#asignacion de elementos boton y barra de busqueda
search_box = driver.find_element(by=By.NAME , value="sSearch")
#submint_button = driver.find_element(by=By.CSS_SELECTOR ,value="Go")
#pruebas--------------------------
submint_button = driver.find_element(By.XPATH, "//form[@id='topsearch']/input[1]")

#----------------------------------


#acciones de los elementos 
search_box.send_keys('samsung')
submint_button.click()




time.sleep(10)
driver.quit()
#--------------------------------------