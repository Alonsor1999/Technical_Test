import os
import sys
import time
import getpass
import subprocess
import pyautogui as Robot
from data.data_pages import Data
from selenium.webdriver.common.keys import Keys

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.common.by import By
from utils.wait import wait_for_element_visible


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.FirstName = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input")
        self.LastName = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[4]/input")
        self.Email = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div[2]/input")
        self.Radio = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[1]")
        self.Mobile = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/input")
        self.dateBirth = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[1]/div/input")
        self.subject = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div[2]/div/div/div[1]/div[2]/div/input")
        self.Hobbies = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[2]")
        self.Address = (By.ID, "currentAddress")
        self.state = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div[2]/div")
        self.city = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[3]/div/div/div[2]/div")
    

    def upload_document(self):
        # Ejecutar tu código JavaScript
        script = """
        var a = document.getElementById("uploadPicture");
        a.click();
        """

        self.driver.execute_script(script)


    def fill_form(self, firstName, lastName, email, mobile, dateBirth, subject, address, state, city):
        try:
            routeFinal = f"C:\\Users\\{Data.user}\\Documents\\File.docx"

            FirstName_input = wait_for_element_visible(self.driver, self.FirstName)
            FirstName_input.send_keys(firstName)

            LastName_input = wait_for_element_visible(self.driver, self.LastName)
            LastName_input.send_keys(lastName)

            Email_input = wait_for_element_visible(self.driver, self.Email)
            Email_input.send_keys(email)

            radio_button = wait_for_element_visible(self.driver, self.Radio)
            radio_button.click()

            time.sleep(0.5)

            Mobile_input = wait_for_element_visible(self.driver, self.Mobile)
            Mobile_input.send_keys(mobile)

            date_of_birth_input = wait_for_element_visible(self.driver, self.dateBirth)
            date_of_birth_input.send_keys(Keys.CONTROL + "a")
            date_of_birth_input.send_keys(dateBirth)
            date_of_birth_input.send_keys(Keys.ENTER)

            Subject_input = wait_for_element_visible(self.driver, self.subject)
            Subject_input.send_keys(subject)
            Subject_input.send_keys(Keys.ENTER)

            time.sleep(1)

            hobbies_button = wait_for_element_visible(self.driver, self.Hobbies)
            self.driver.execute_script("arguments[0].scrollIntoView();", hobbies_button)
            hobbies_button.click()

            self.upload_document()
            time.sleep(1)
            Robot.typewrite(routeFinal)
            Robot.press("enter")

            time.sleep(0.5)
            Address_input = wait_for_element_visible(self.driver, self.Address)
            Address_input.send_keys(address)
 
            state_button = wait_for_element_visible(self.driver, self.state)
            state_button.click()
            time.sleep(0.5)
            Robot.typewrite(state)
            Robot.press('enter')

            city_button = wait_for_element_visible(self.driver, self.city)
            city_button.click()
            time.sleep(0.5)
            Robot.typewrite(city)
            Robot.press('enter')

        except Exception as e:
            print("Error", e)