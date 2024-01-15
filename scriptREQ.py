import os
import time
import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#----------CONFIGURACION-----------------
#cambiar ruta de su chrome driver y el navegador que usen esto solo para chrome drive local
#LINUX
#driver = webdriver.Chrome('/usr/bin/chromedriver')
#WINDOWS
#driver = webdriver.chrome('C:/Users/lusena/Documents/chromedriver-win64/chromedriver')
# Inicializar el escritor CSV
escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
nombre_archivo = os.path.join(escritorio, 'resultados.csv')
# Verificar si el archivo existe y borrarlo si es necesario
if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
# Definir los encabezados del CSV
campos = ["Modelo", "Fecha de Salida", "OS", "Cuerpo", "Almacenamiento", "Size", "Res", 
              "Cámara", "Ram", "Cpu", "Batería", "Network", "Link imagen"]
if not os.path.isfile(nombre_archivo):
    # Si no existe, crea el archivo y escribe los encabezados
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()

#CHROME DRIVE EN LINEA CON EDGE
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#url gsmarena
driver.get('http://www.gsmarena.com/');
#selecionar archivo csv
df = pd.read_csv('C:\\Users\\lusena\\Downloads\\TAC11_1_2024 - tac_202401041229.csv')
'''
salida = "none"
Os = "none"
cuerpo  = "none"
almacen  = "none"
size  = "none"
res  = "none"
camara = "none"
ram  = "none"
cpu  = "none"
Bateria  = "none"
Network = "none"
link_de_la_imagen = "none"
'''
def imprecionGeneracionDeCsv(modelo,salida,Os,cuerpo,almacen,size,res,camera,ram,cpu,Bateria,Network,link_de_la_imagen):
 try:
    with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo_csv:
      escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
      escritor_csv.writerow({
            "Modelo": str(modelo),
            "Fecha de Salida": str(salida),
            "OS": str(Os),
            "Cuerpo": str(cuerpo),
            "Almacenamiento": str(almacen),
            "Size": str(size),
            "Res": str(res),
            "Cámara": str(camera),
            "Ram": str(ram),
            "Cpu": str(cpu),
            "Batería": str(Bateria),
            "Network": str(Network),
            "Link imagen": str(link_de_la_imagen)
        })
      
    print("------------Extraccion de Datos----------------")
    print("Modelo:", str(modelo)if modelo else None)
    print("Fecha de Salida:", str(salida))
    print("OS:", str(Os))
    print("Cuerpo:",str(cuerpo))
    print("Almacenamiento:", str(almacen))
    print("Size:", str(size))
    print("Res:", str(res))
    print("Cámara:",str(camera), "mp")
    print("Ram:", str(ram),"gb ram")
    print("Cpu:", str(cpu))
    print("Batería:", str(Bateria), "mAh")
    print("Network:", str(Network))
    print("Link imagen:",str(link_de_la_imagen))
    print("------------Fin de Extraccion-----------------")
 except Exception as e:
    print(f"Error: {e}")  


def busquedaPagina():
    try:
        # Espera a que el elemento esté presente en la página
        #clic primer articulo de la lista
        li_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/ul/li[1]/a'))   
        )
        li_element.click()


        #Extraccion del link de la imagen
        img_element = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/a/img')
        link_de_la_imagen = img_element.get_attribute('src')
        #Extraccion del modelname
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
        Os = OS_element.text
        #Extraccion del storage-hl
        storage_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[1]/span[4]/span')
        almacen = storage_element.text
        #Extraccion del displaysize-hl displayres-hl
        size_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[4]/strong/span')
        size = size_element.text
        res_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[4]/div')
        res = res_element.text
        #Extraccion del camerapixels-hl "mp" videopixels-hl "p"
        cameramp_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[5]/strong/span[1]')
        camera = cameramp_element.text
        #Extraccion del ramsize-hl "gb ram"  chipset-hl
        ramsize_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[6]/strong/span[1]')
        ram = ramsize_element.text
        cpu_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[6]/div')
        cpu = cpu_element.text
        #Extraccion del batsize-hl "mAh"  battype-hl
        bat_element = driver.find_element(By.XPATH,'//*[@id="body"]/div/div[1]/div/div[2]/ul/li[7]/strong/span[1]')
        Bateria = bat_element.text
        #Extraccion del networck
        network_element = driver.find_element(By.XPATH,'//*[@id="specs-list"]/table[1]/tbody/tr[1]/td[2]/a')
        Network = network_element.text



    except Exception as e:
        print(f"Error: {e}")   
    
    imprecionGeneracionDeCsv(modelo,salida,Os,cuerpo,almacen,size,res,camera,ram,cpu,Bateria,Network,link_de_la_imagen)

     #time.sleep(2)
     #generar CSV
        
    #--------------------------------------

def busquedaGoogle(Marca1,Modelo1):
   print("El objeto fue llamado con éxito.")
   driver1 = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
   driver1.get('https://www.google.com')
   buscar1 = driver1.find_element(by= By.ID , value= "APjFqb")
   buscar1.send_keys(Marca1," ",Modelo1)
   buscar1.send_keys(Keys.ENTER)
   driver1.quit()

#-------------CODIGO----------------
time.sleep(1)
for index, row in df.iterrows():
 #search_box.clear()
 marca = row['mark']
 modelo = row['model']
 #asignacion de elementos boton y barra de busqueda 
 #asignamos la barra de busqueda  mendiante su identificador NAME
 search_box = driver.find_element(by=By.NAME , value="sSearch")
 #limpiar caja de busqueda
 search_box.clear()
 #enviamos el el modelo de marca a la barra de busqueda
 #search_box.send_keys(marca," ",modelo)
 search_box.send_keys(modelo," ",marca)
 #creamos un evento del tipo send key en este caso enter del mismo modo buscamos medianta XPATH el elemento input de la barra de busqueda
 submit_button = driver.find_element(By.XPATH, "//form[@id='topsearch']/input[1]")
 submit_button.send_keys(Keys.ENTER)
 

 #filtro si no encuentra el resultado

 try:
    avisoNoEncontroElemento = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="news"]/h3'))   
            )
    #mensaje = avisoNoEncontroElemento.find_element(By.XPATH, '//*[@id="body"]/div/div[1]/div/div[1]/h1')
    mensaje = avisoNoEncontroElemento.text
    if mensaje == "News":
       
        busquedaPagina()

    else:
        busquedaGoogle(marca, modelo)
        print("No se encontro el dato")
   
 except Exception as e:
       print(f"Error: {e}") 
       

time.sleep(1)
print("-----BUSQUEDA FINALIZDA Archivo CSV Generado en escritorio---------")
driver.quit()
#-------------FIN DEL CODIGO----------------
#print(df.columns)
#primer_modelo = df['model'].iloc[0]
#print("primer modelo:", primer_modelo)