import socket
import threading

HOST = '127.0.0.1'  # Server address
PORT = 5000         # Port to listen on

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
                client_socket.close()  # Close the socket when client disconnects
                break
        except:
            print(f"Connection closed from {client_address}")
            clients.remove(client_socket)
            client_socket.close()  # Close the socket when client disconnects
            

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
# Accept new client connections and start a thread for each client
# def accept_clients():
#     while True:
#         client_socket, client_address = server_socket.accept()
#         print(f"New connection from {client_address}")
#         clients.append(client_socket)
        
#         # Start a new thread to handle this client
#         client_thread = threading.Thread(target=handle_client, args=(client_socket,))
#         client_thread.start()

# # Run the server to accept clients
# accept_clients()