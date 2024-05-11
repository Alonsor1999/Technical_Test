import socket, os, ctypes, psutil

import os
import sys
import subprocess

# Agrega el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import socket
import json


class IdentifyPortInit:
    def identifyPortAsInit():
        try:
            host = '127.0.0.1'  # Puedes cambiarlo a '0.0.0.0' para aceptar conexiones desde cualquier dirección IP
            port = 19185
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            print(f"El puerto {port} está abierto en {host}")
            sock.close()
            print('Puerto cerradoc orrectamente')
        except (socket.timeout, ConnectionRefusedError):
            pass

        # Dirección IP y puerto en el que deseas que el servidor escuche
        host = '127.0.0.1'  # Puedes cambiarlo a '0.0.0.0' para aceptar conexiones desde cualquier dirección IP
        port = 19185

        # Crea un objeto socket para el servidor
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Asocia el socket del servidor a la dirección y puerto especificados
            server_socket.bind((host, port))

            # Escucha por conexiones entrantes (hasta 5 conexiones en espera)
            server_socket.listen(5)
            print("Servidor escuchando en {}:{}...".format(host, port))

            while True:
                # Acepta una nueva conexión del cliente
                client_socket, client_address = server_socket.accept()
                print("Cliente conectado desde:", client_address)

                # Recibe el mensaje del cliente
                data = client_socket.recv(4096).decode()
                print("Mensaje del cliente:", data)
                objeto = json.loads(data)

                if objeto["closeApp"] == True:
                    print('close')
                    ctypes.windll.user32.MessageBoxW(0, "Cerra todas las sesiones abiertas en los navegadores!", "Alerta", 0x40 | 0x1)

                    print('cierre init')

                    # Cierra la consola
                    os._exit(0)

                # typeDocument = objeto["typeDocument"]
                # Document = objeto["Document"]
                # print(typeDocument)

                # print(type(data))
                # type_document_valor1= data['Document']
                # print(type_document_valor1)
                # Envía una respuesta al cliente
                response = "¡Hola, cliente!"
                client_socket.sendall(response.encode())
                
                # Cierra la conexión del cliente
                client_socket.close()
                # return objeto
                return objeto

        except Exception as e:
            print("Error en el servidor:", e)

        finally:
            # Cierra el socket del servidor cuando hayas terminado
            server_socket.close()

class IdentifyPort:
    def __init__(self, driver):
        self.driver = driver

    def identifyPortAs(self):
        try:
            host = '127.0.0.1'  # Puedes cambiarlo a '0.0.0.0' para aceptar conexiones desde cualquier dirección IP
            port = 19185
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            print(f"El puerto {port} está abierto en {host}")
            sock.close()
            print('Puerto cerrado orrectamente')
        except (socket.timeout, ConnectionRefusedError):
            pass

        while True:
            # Dirección IP y puerto en el que deseas que el servidor escuche
            host = '127.0.0.1'  # Puedes cambiarlo a '0.0.0.0' para aceptar conexiones desde cualquier dirección IP
            port = 19185

            # Crea un objeto socket para el servidor
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                # Asocia el socket del servidor a la dirección y puerto especificados
                server_socket.bind((host, port))

                # Escucha por conexiones entrantes (hasta 5 conexiones en espera)
                server_socket.listen(5)
                print("Servidor escuchando en {}:{}...".format(host, port))

                while True:
                    # Acepta una nueva conexión del cliente
                    client_socket, client_address = server_socket.accept()
                    print("Cliente conectado desde:", client_address)

                    # Recibe el mensaje del cliente
                    data = client_socket.recv(4096).decode()
                    print("Mensaje del cliente:", data)
                    objeto = json.loads(data)

                    if objeto["closeApp"] == True:
                        print('close')
                        ctypes.windll.user32.MessageBoxW(0, "Cerra todas las sesiones abiertas en los navegadores!", "Alerta", 0x40 | 0x1)

                        self.driver.quit()

                        print('cierre')

                        # Cierra la consola
                        os._exit(0)

            except Exception as e:
                print("Error en el servidor:", e)