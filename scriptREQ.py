import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#----------CONFIGURACION-----------------
#cambiar ruta de su chrome driver y el navegador que usen
#linux
#driver = webdriver.Chrome('/usr/bin/chromedriver')
#windows
#driver = webdriver.chrome('C:/Users/lusena/Documents/chromedriver-win64/chromedriver')
#chrome driver en linea
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#url gsmarena
driver.get('http://www.gsmarena.com/');


#-------------CODIGO----------------
time.sleep(5)
#introduciendo datos a la barra de buscador
#search_box = driver.find_element_by_name("sSearch")
search_box = driver.find_element(by=By.NAME , value="sSearch")
search_box.send_keys('samsung')

time.sleep(5)
driver.quit()
#--------------------------------------