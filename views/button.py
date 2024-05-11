import os
import sys
import pyautogui as Robot
import time
import subprocess
from selenium.webdriver.common.keys import Keys

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By
from utils.wait import wait_for_element_visible


class ButtonPage:

    def __init__(self, driver):
        self.driver = driver
        self.button = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[11]/div/button')        
    
    def actionButton(self):
        try:
           
           submit = wait_for_element_visible(self.driver, self.button)
           self.driver.execute_script("arguments[0].scrollIntoView();", submit)
           submit.click()
        
        except Exception as e:
            print("Error", e)