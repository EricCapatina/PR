import socket
import os

host = '127.0.0.1'
port = 1337
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("Introdu ceva")
home_folder = os.path.dirname(os.path.abspath(__file__))

if ".png" in msg:
    stats = os.stat(msg)
    message = "Uploaded image with size: " + str(stats.st_size)
    try:
        sock.sendto(message.encode("utf-8"), (host, port))
    except socket.error:
        print(str(socket.error))
    data, addr = sock.recvfrom(4096)
    sock.close()
else:
    message = "Received a message from client: " + msg
    try:
        sock.sendto(message.encode("utf-8"), (host, port))
    except socket.error:
        print(str(socket.error))
    data, addr = sock.recvfrom(4096)
    sock.close()
