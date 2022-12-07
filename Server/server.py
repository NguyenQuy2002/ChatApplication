import socket
import threading

# Server IP and Port
HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client = []
names = []

def broadcast(message):
    for clients in client:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)
            
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
        clients, address = server.accept()
        print(f'Connected with {str(address)}')
        clients.send('Name'.encode('ascii'))
        name = clients.recv(1024).decode('ascii')
        names.append(name)
        clients.send('Connected to the server'.encode('ascii'))
        broadcast(f'{name} joined the chat'.encode('ascii'))
        client.append(clients)
        thread = threading.Thread(target=handle_client, args=(clients,))
        thread.start()
    
    
print('Server is listening...')
receive()
server.close()

