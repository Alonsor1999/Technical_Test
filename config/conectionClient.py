import socket
import json
import time
# import ConsultaTitularidadH

from data.data_pages import Data

def clientAs():
    host = "127.0.0.1"  # La dirección IP del servidor C# (reemplaza con la IP del servidor)
    port = 14444        # El puerto del servidor C# (reemplaza con el puerto del servidor)

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Conexión establecida con el servidor.")

        data =  {
        "NameClient": Data.NameClient,
        "QuantityGB": Data.QuantityGB,
        "AddGB": Data.AddGB,
        "SalePrice": Data.SalePrice,
        "OldPrice": Data.OldPrice,
        "Phone": Data.Phone,
        "Quota": Data.Quota,
        "OpticalFiber": Data.OpticalFiber,
        "WrongUser": Data.WrongUser,
        "UpgradePos": Data.UpgradePos,
        "MobileTerminal": Data.MobileTerminal,
        "FixedTotalization": Data.FixedTotalization,
        "AdditionalPos": Data.AdditionalPos,
        "message": Data.message
        }

        # Convertir el diccionario a una cadena JSON
        json_data = json.dumps(data)

        print(json_data)

        # Enviar la cadena JSON al servidor
        client_socket.sendall(json_data.encode())

        # Recibir la respuesta del servidor
        response = client_socket.recv(8192)
        print("Respuesta del servidor: {}".format(response.decode()))

        client_socket.close()
        print("Conexión cerrada.")
    except Exception as e:
        print("Error en el cliente: {}".format(e))