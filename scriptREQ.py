import time
from selenium import webdriver

#----------CONFIGURACION-----------------
#cambiar ruta de su chrome driver y el navegador que usen
driver = webdriver.Chrome('/usr/bin/chromedriver')
#url gsmarena
driver.get('http://www.gsmarena.com/');


#-------------CODIGO----------------
time.sleep(5)
#introduciendo datos a la barra de buscador
search_box = driver.find_element_by_name('sSearch')
search_box.send_keys('samsung')
search_box.send_keys(Keys.RETURN)
search_box.submit()
time.sleep(5)
driver.quit()
#--------------------------------------