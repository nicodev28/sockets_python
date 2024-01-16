# Sockets : client

import socket
import time

# Variables

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

# Connection to the server

print(f"Attente de connexion au serveur {HOST_IP}, port {HOST_PORT} ...")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print("ERREUR : connexion au serveur impossible")
        time.sleep(4)
    else:
        print(f"Connexion établie sur le serveur")
        break

# Data exchange

while True:
    data_receive = s.recv(MAX_DATA_SIZE)
    print(f"Message: {data_receive.decode()}")
    texte_envoye = input("Vous:")
    s.sendall(texte_envoye.encode())

s.close()