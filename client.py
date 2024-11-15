import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT =  5000       # Port to listen on (non-privileged ports are > 1023)

def send_messages(client_socket):
    while True:
        try:
            message = input("You: ")
            if message.lower() == 'exit':  # Type 'exit' to disconnect
                print("Disconnecting from server.")
                client_socket.close()
                break
            client_socket.send(message.encode())
        except Exception as e:
            print("Error sending message:", e)
            client_socket.close()
            break

            
def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
            else:
                print("Server connection closed.")
                client_socket.close()
                break
        except Exception as e:
            print("Error receiving message:", e)
            client_socket.close()
            break

# def start_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         try:
#             client_socket.connect((HOST, PORT))
#             print("Connected to the server!")

#             # Start send and receive threads
#             threading.Thread(target=send_messages, args=(client_socket,)).start()
#             threading.Thread(target=receive_messages, args=(client_socket,)).start()

#         except ConnectionRefusedError:
#             print("Connection refused. Is the server running?")
#         except Exception as e:
#             print("An error occurred:", e)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        client_socket.connect((HOST, PORT))
        print("Connected to server!")
        
        while True:
            message = input("You: ")
            if message.lower() == 'exit':
                print("Disconnecting from server.")
                break
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            print(f"Server: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

# if __name__ == "__main__":
#     start_client()
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((HOST, PORT))
#     print("Connected to the server!")

#     # Start send and receive threads
#     threading.Thread(target=send_messages, args=(client_socket,)).start()
#     threading.Thread(target=receive_messages, args=(client_socket,)).start()

# except ConnectionRefusedError:
#     print("Connection refused. Is the server running?")
# except Exception as e:
#     print("An error occurred:", e)