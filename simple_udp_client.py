
import socket

target_host = "127.0.0.1"
target_port = 9997

# Create a socket object
# AF_INET parameter indicates that we will use a standard IPV4 address or hostname
# SOCK_DGRAM indicates that this will be a UDP client


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Does not connect as UDP is a connectionless protocol

# Send some data as a string

client.sendto(b"AAABBBCCC", (target_host, target_port))

# Recieve some data back, print out response and close the socket

data, addr = client.recvfrom(4096)

print(data.decode())

client.close()
