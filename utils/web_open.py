import os
import sys

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from config.config import Config
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Crear una instancia del controlador de Selenium
# chrome_driver_path = 'C:\\BotsTelefonicaNBA\\NBA_RPA\\_internal\\chromedriver-win32\\chromedriver.exe'


def webOpen():
    # Configura las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")  # Desactiva la barra de información
    chrome_options.add_argument("--disable-extensions")  # Desactiva las extensiones
    chrome_options.add_argument("start-maximized")  # Desactiva las extensiones
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Excluye la switch de automatización
    chrome_options.add_experimental_option('useAutomationExtension', False)  # Desactiva la extensión de automatización
    
    # Configura el WebDriver para Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # # se navega a la URL indicada
    driver.get(Config.PAGE_URL)
    # Al abrir el navegador se maximize

    return driver