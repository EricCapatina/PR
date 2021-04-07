import socket
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
target_host = "127.0.0.1"
target_port = 1337
client_socket = socket.socket()

try:
    client_socket.connect((target_host, target_port))
except socket.error:
    print(str(socket.error))

server_response = client_socket.recv(1024)
print("Response from server: " + server_response.decode("utf-8"))

while True:
    client_message = input("Introdu ceva\n\t\t\t")
    client_socket.send(str.encode(client_message))
    response_from_server = client_socket.recv(1024)
    print(current_time + ": " + response_from_server.decode("utf-8"))
client_socket.close()
