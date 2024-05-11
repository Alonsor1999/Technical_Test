import os
import sys
import time
import subprocess
import pandas as pd
import pyautogui as Robot
from selenium.webdriver.common.keys import Keys

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By
from utils.wait import wait_for_element_visible


class TablePage:

    def __init__(self, driver):
        self.driver = driver


    def extractionTable(self):
        try:
           # Localiza el cuerpo de la tabla
            filas = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'rt-tbody')]//div[@role='row']")

            # Lista para almacenar los datos
            datos = []

            # Iterar sobre cada fila
            for fila in filas:
                gridcells = fila.find_elements(By.XPATH, ".//div[@role='gridcell']")
                
                if len(gridcells) >= 4:  # Asegura que haya al menos 4 gridcells
                    
                    titulo = gridcells[1].find_element(By.TAG_NAME, 'span').text
                    autor = gridcells[2].text
                    editor = gridcells[3].text
                    
                    # Añadir al diccionario
                    datos.append({
                        
                        'Title': titulo,
                        'Author': autor,
                        'Publisher': editor
                    })

            # Cierra el navegador una vez finalizado
            self.driver.quit()
            # Crear DataFrame de Pandas
            df = pd.DataFrame(datos)

            # Obtener el path del escritorio del usuario actual
            desktop_path = os.path.join(os.path.expanduser("~"), "Documents")

            # Nombre del archivo Excel
            excel_file = os.path.join(desktop_path, 'datos_extraidos.xlsx')

            # Guardar DataFrame en archivo Excel
            df.to_excel(excel_file, index=False)

            # Imprimir la ruta donde se guardó el archivo y mostrar los datos extraídos
            print(f"Archivo guardado en: {excel_file}")
            print(df)


        except Exception as e:
            print("Error", e)