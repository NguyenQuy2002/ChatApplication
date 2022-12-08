

import socket
import threading

# Server IP and Port
HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
names = []

#send message to all client
def broadcast(message):
    for client in clients:
            try:
                client.send(message)
            except:
                clients.close()
                remove(client)
            
# Create a socket object
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            client.remove(client)
            client.close()
            name = name[index]
            broadcast(f'{name} left the chat'.encode('ascii'))
            break
    

def receive():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        client.send('Name'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        names.append(name)
        client.send('Connected to the server'.encode('ascii'))
        broadcast(f'{name} joined the chat'.encode('ascii'))
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
    
    
print('Server is listening...')
receive()
server.close()
