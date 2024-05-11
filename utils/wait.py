import os
import sys

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config


def wait_for_element_visible(driver, locator, timeout=Config.WAIT_TIME):
    """
    Espera hasta que el elemento esté visible.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((locator)))
        return element
    except:
        pass

def wait_for_element_visible_one(driver, locator, timeout=Config.WAIT_TIME_ONE):
    """
    Espera hasta que el elemento esté visible y si no se hace visible en 5 segundos vuelva a hacer el procedimiento.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((locator)))
        return element
    except:
        return False
    
def wait_for_elements_visible(driver, locator, timeout=120):
    """
    Espera hasta que el elemento esté visible.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_all_elements_located((locator)))
        return element
    except:
        raise Exception(f"El elemento con el localizador {locator} no es visible después de {timeout} segundos.")
    
def wait_for_element_presence(driver, locator, timeout=10):
    """
    Espera hasta que el elemento esté visible.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator)))
        return element
    except:
        raise Exception(f"El elemento con el localizador {locator} no es visible después de {timeout} segundos.")
    
def wait_for_element_visible_three_repeat_function_(driver, locato1, locator2, Locator3, timeout=0):
    """
    Espera hasta que el elemento esté visible.
    """
    count = 0
    while True:
        if count < 120:
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((locato1)))
                return '1'
            except:
                pass
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((locator2)))
                return '2'
            except:
                pass
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((Locator3)))
                return '3'
            except:
                pass
        else:
            break

def wait_for_element_visible_two_repeat_function_(driver, locato1, timeout=0):
    """
    Espera hasta que el elemento esté visible.
    """
    count = 0
    while True:
        if count < 120:
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((locato1)))
                return True
            except:
                if count == 2:
                    return False
                pass

        else:
            break
  
        count += 1

# def wait_for_element_pyautogui(locator):
#     contador = 0
#     while True:
#         time.sleep(1)
#         img = pyautogui.locateCenterOnScreen(locator, confidence=0.95)
#         if img is not None:
#             return img
#         if contador > 120:
#             print("No se encontró el objeto en la página web.")
#             break
#         contador += 1

# def wait_for_element_pyautogui_revert(locator):
#     contador = 0
#     while True:
#         time.sleep(1)
#         img = pyautogui.locateCenterOnScreen(locator, confidence=0.95)
#         if img is None:
#             break
#         if contador > 10:
#             break
#         contador += 1