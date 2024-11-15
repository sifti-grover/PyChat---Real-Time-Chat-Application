import socket
import threading

HOST = '127.0.0.1'  
PORT = 5000        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT)) 
server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}")

clients = []

def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    clients.append(client_socket)
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Message from : {message}")
                broadcast(message, client_socket)
            else:
                clients.remove(client_socket)
                client_socket.close()  
                break
        except:
            print(f"Connection closed from {client_address}")
            clients.remove(client_socket)
            client_socket.close() 
            

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

while True:
    client_socket, client_address = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
