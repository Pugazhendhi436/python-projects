import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello UDP Server".encode(), ('localhost', 5001))

data, addr = client.recvfrom(1024)

print(data.decode())

client.close()
