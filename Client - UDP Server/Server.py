import socket

host = '127.0.0.1'
port = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

while True:
    data, addr = sock.recvfrom(1024)
    if data is None:
        continue
    else:
        data = data.decode('utf-8')
        print(data)
