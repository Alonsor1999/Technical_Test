import socket
import json

from data.data_pages import Data  # Supongo que esto importa la clase Data donde se almacenan los datos

def serverAsLogin():
    # Dirección IP y puerto en el que deseas que el servidor escuche
    host = '127.0.0.1'  # Puedes cambiarlo a '0.0.0.0' para aceptar conexiones desde cualquier dirección IP
    port = 15201

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

            # Actualiza los datos en la clase Data
            Data.USERNAME = objeto["username"]
            Data.PASSWORD = objeto["password"]
            # Data.TYPESEARCH = objeto["searchFor"]
            # Data.NUMBER = objeto["queryNumber"]

            # Cierra la conexión del cliente
            client_socket.close()

            # Retorna los datos procesados
            return {
                "username": Data.USERNAME,
                "password": Data.PASSWORD,
                # "searchFor": Data.TYPESEARCH,
                # "queryNumber": Data.NUMBER
            }

    except Exception as e:
        print("Error en el servidor:", e)

    finally:
        # Cierra el socket del servidor cuando hayas terminado
        server_socket.close()

# if _name_ == "main":
# main1()