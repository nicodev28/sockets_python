# Sockets réseau : server

import socket

# Variables

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

# server launch

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT} ...")
connection_socket, client_address = s.accept()
print(f"Connexion établie avec {client_address}")

# Data exchange

while True:
    texte_envoye = input("Vous: ")
    connection_socket.sendall(texte_envoye.encode())
    data_receive = connection_socket.recv(MAX_DATA_SIZE)
    print(f"Message: {data_receive.decode()}")


s.close()