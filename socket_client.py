import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(('localhost', 5000))

# Send message
client.send("Hello Server!".encode())

# Receive response
response = client.recv(1024).decode()

print("Server says:", response)

# Close connection
client.close()