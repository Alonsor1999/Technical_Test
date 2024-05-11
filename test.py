import os
import sys
import time
import pymsgbox
import ctypes, threading

from selenium.webdriver.common.keys import Keys

# Obtener el identificador de la ventana de la consola
console_handle = ctypes.windll.kernel32.GetConsoleWindow()

# Minimizar la ventana de la consola
ctypes.windll.user32.ShowWindow(console_handle, 6)

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By

# paginas
# from views.login import LoginPage
from views.form import FormPage
from views.button import ButtonPage
from views.extractiontable import TablePage
from views.createfile import CreateFile

# data
from data.data_pages import Data

from config.config import Config
from config.conectionServer import serverAs
from config.conectionClient import clientAs
from config.conectionServerLogin import serverAsLogin

from utils.web_open import webOpen

CreateFile()
doc_path = os.path.expanduser("~/Documents/File.docx")

# Verificar si el archivo ya existe antes de intentar abrir el navegador
if os.path.exists(doc_path):
    try:
        driver = webOpen()
        
        form_page = FormPage(driver)
        form_page.fill_form(Data.USERNAME, Data.LASTNAME, Data.EMAIL, Data.MOBILE, Data.DATEBIRTH, Data.SUBJECT, Data.ADDRESS, Data.STATE, Data.CITY)

        time.sleep(0.5)

        button_page = ButtonPage(driver)
        button_page.actionButton()

        time.sleep(1)

        # Abrir una nueva pestaña
        driver.execute_script("window.open('');")
        # Cambiar el enfoque a la nueva pestaña
        driver.switch_to.window(driver.window_handles[1])
        # Cargar una nueva URL en la nueva pestaña
        driver.get(Config.TABLE_PAGE_URL)

        extraction_page = TablePage(driver)
        extraction_page.extractionTable()

        input("la Ejecución se hizo correctamente")

    except Exception as e:
        print("error", e)
else:
    mensaje = "¡La ejecucion no puede continuar, comuniquese con el Administrador"
    pymsgbox.alert(mensaje, "Error")

    



