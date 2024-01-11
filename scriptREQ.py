import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
submit_button = driver.find_element(By.XPATH, "//form[@id='topsearch']/input[1]")
#selector_button = driver.find_element(By.XPATH, "//a[@id = '']")
#pruebas--------------------------
li_element = driver.find_element(By.XPATH, "//div[@id='review-body']/div[@class='makers']/ul")


#----------------------------------


#acciones de los elementos 
search_box.send_keys('M1803E7SG')
submit_button.send_keys(Keys.ENTER)
li_element.click()





time.sleep(10)
driver.quit()
#--------------------------------------