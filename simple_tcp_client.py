
import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
# AF_INET parameter indicates that we will use a standard IPV4 address or hostname
# SOCK_STREAM indicates that this will be a TCP client


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server

client.connect((target_host, target_port))

# Send some data as bytes

client.send(b"GET / HTTP/1.1\r\nHOST:google.com\r\n\r\n")

# Recieve some data back, print out response and close the socket

response = client.recv(4096)
print(response.decode())
client.close()
