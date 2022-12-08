'''
TODO:
Add private text messages (Pasar los nicknames a client.py)

Add admin privileges

Add game
'''

import threading
import socket
from colorama import Fore, Back, Style
import time

host = 'localhost'
port = 58000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Broadcast messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle messages from clients
def handle_client(client):
    while True:
        try:
            # Broadcast messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove and close clients that disconnect
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat\n'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Receive / broadcast messages
def receive():
    while True:
        if(len(clients) == 1):
            administrator = clients[0]
            time.sleep(0.5)
            administrator.send('You are the administrator\n'.encode('utf-8'))

        # Accept connection
        print('Server listening...')
        client, address = server.accept()
        print(f'Connection established with {str(address)}')

        # Request and store nickname
        nickname = client.recv(1024).decode('utf-8')
        # Remove the ': \n' from the nickname
        nickname = nickname[:-4]

        print(nickname)
        nicknames.append(nickname)
        clients.append(client)

        # Print and broadcast nickname
        print(' The nickname of the client is ' + Fore.GREEN + f'{nickname}' + Style.RESET_ALL)
        print(nickname)
        client.send('Now connected to the server\n'.encode('utf-8'))
        broadcast(f'{nickname} has joined the chat \n'.encode('utf-8'))

        # Start handling thread for client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    receive()