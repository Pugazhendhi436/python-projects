import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('localhost', 5001))

print("UDP Server running...")

data, addr = server.recvfrom(1024)

print("Message:", data.decode())

server.sendto("Hello UDP Client".encode(), addr)

server.close()