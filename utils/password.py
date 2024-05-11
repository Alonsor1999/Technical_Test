import os
import sys
import subprocess

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By
from utils.wait import wait_for_element_visible_one

from config.conectionClient import clientAs

# data
from data.data_pages import Data


class Password:

    def __init__(self, driver):
        self.driver = driver
        self.failed = (By.XPATH, '//*[text()="*Cuenta o contraseña erronea"]')


    def passwordAs(self):
        failed = wait_for_element_visible_one(self.driver, self.failed)

        if failed != False:
            failed = failed.text

        if failed == '*Cuenta o contraseña erronea':
            Data.WrongUser = True
            clientAs()

            return True
        else:
            return False

