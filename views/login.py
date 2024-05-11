import os
import sys
import subprocess

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By
from utils.wait import wait_for_element_visible


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        # self.username_input = (By.ID, 'inputUser')
        # self.username_input = (By.XPATH, '//*[@id="account"]')
        self.username_input = (By.XPATH, "/html/body/app-root/app-login/div/div/form/mat-form-field[1]/div[1]/div/div[2]/input")
        # self.password_input = (By.ID, 'password')
        self.password_input = (By.XPATH, "/html/body/app-root/app-login/div/div/form/mat-form-field[2]/div[1]/div/div[2]/input")
        self.login_button = (By.XPATH, "/html/body/app-root/app-login/div/div/form/button")


    def loginAs(self, username, password):
        username_input = wait_for_element_visible(self.driver, self.username_input)
        # username_input.clear()
        username_input.send_keys(username)

        password_input = wait_for_element_visible(self.driver, self.password_input)
        # password_input.clear()
        password_input.send_keys(password)

        # login_button = wait_for_element_visible(self.driver, self.login_button)
        # # login_button.click()
        # self.execute_script("arguments[0].click();", login_button)
