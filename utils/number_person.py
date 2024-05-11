from getpass import getuser
import os
import io

def data_number_person():
    # Ruta del archivo txt
    username = getuser()
    file_path = os.path.abspath("C:\\Users\\" + username + "\\Documents\\MovistarExecute.txt")

    # Abre el archivo txt usando io
    with io.open(file_path, mode="r", encoding="utf-8") as file:
        # Lee el contenido del archivo
        phone = file.readline().strip()
        user = file.readline().strip()
        passworld = file.readline().strip()

        return phone, user, passworld
    # print(phone)
    # print(user)
    # print(passworld)
    # return content
    