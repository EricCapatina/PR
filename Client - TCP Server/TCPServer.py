import socket
import _thread
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
host = "127.0.0.1"
port = 1337
server_socket = socket.socket()
thread_count = 1

try:
    server_socket.bind((host, port))
except socket.error:
    print(str(socket.error))
server_socket.listen(5)


def Clients(number, thread_name):
    number.send(str.encode("Connected to TCP server, now here are connected: " + str(thread_count - 1)
                           + " clients!"))
    while True:
        data = number.recv(1024)
        server_response = data.decode('utf-8')
        if not data:
            break
        print(thread_name + " Client message:\tTime: " + current_time + " Message: " + server_response)
        number.sendall(str.encode(server_response))
    number.close()


while True:
    client, address = server_socket.accept()
    _thread.start_new_thread(Clients, (client, "Thread " + str(thread_count)))
    print("Thread " + str(thread_count) + ": " + "Connected address: " + address[0] + " port: " + str(address[1]))
    thread_count += 1
server_socket.close()
