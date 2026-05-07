import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to host and port
server.bind(('localhost', 5000))

# Listen for connections
server.listen(1)

print("Server waiting for connection...")

# Accept connection
client_socket, addr = server.accept()

print("Connected to:", addr)

# Receive data
message = client_socket.recv(1024).decode()
print("Client says:", message)

# Send response
client_socket.send("Hello Client!".encode())

# Close connection
client_socket.close()
server.close()