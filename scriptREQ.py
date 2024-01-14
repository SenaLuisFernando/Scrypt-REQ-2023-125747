import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
search_box.send_keys('RNE-L03')
submit_button = driver.find_element(By.XPATH, "//form[@id='topsearch']/input[1]")
submit_button.send_keys(Keys.ENTER)


#pruebas----------------------------
try:
    # Espera a que el elemento esté presente en la página
    #clic primer articulo de la lista
    li_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/ul/li[1]/a'))   
    )

    li_element.click()
    #Extraccion del link de la imagen
    img_presente = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/a/img'))
    )
    img_element = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/a/img')
    link_de_la_imagen = img_element.get_attribute('src')

     #Extraccion del modelname
    Extraccion_del_modelname = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div/div[1]/div/div[1]/h1'))
    )
    modelname_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[1]/h1')
    modelo = modelname_element.text
     #Extraccion del released-hl
    released_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[1]/span[1]/span')
    salida = released_element.text
    
     #Extraccion del body-hl
    body_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[1]/span[2]/span')
    cuerpo = body_element.text
     #Extraccion del os-hl
    OS_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[1]/span[3]/span')
    os = OS_element.text
     #Extraccion del storage-hl
    storage_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[1]/span[4]/span')
    almacen = storage_element.text
     #Extraccion del displaysize-hl displayres-hl
     #Extraccion del camerapixels-hl "mp" videopixels-hl "p"
     #Extraccion del ramsize-hl "gb ram"  chipset-hl
     #Extraccion del batsize-hl "mAh"  battype-hl
     #Extraccion del networck



    
    

except Exception as e:
    print(f"Error: {e}")
    

#----------------------------------

time.sleep(10)
print("------------Extraccion de Datos-----------------")
print("Link imagen:",link_de_la_imagen)
print("Modelo:", modelo)
print("Fecha de Salida:", salida)
print("OS:", os)
print("Cuerpo:", cuerpo)
print("Almacenamiento:", almacen)
print("------------Fin de Extraccion-----------------")

driver.quit()
#--------------------------------------