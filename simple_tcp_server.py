
# Import socket and threading modules. Socket provides the base networking functionality required.

import socket
import threading

# Pass in the IP address and port we want the server to listen in on

IP = '0.0.0.0'
PORT = 9998

# We instruct the server to start listening with a maximum backlog of connections set to 5
# Here we specify a standard IPV4 address with AF_INET, and a TCP connection with SOCK_STREAM


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT)) 
    server.listen(5) 
    print(f'[*] Listening on {IP}: {PORT}')
    
# We put the server into its main loop, where it waits for an incoming connection
# When a client connects, we recieve the client socket in the client variable, and the remote connection details in the address variable
# We then create a new thread object that points to our handle_client function, and we pass in the client_socket object as an argument
# We start the thread to handle the client connection here, at this point the main server loop is ready to handle another incoming connection
                                 
    while True:
        client, address = server.accept() 
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

# The handle_client function performs the recv(), and then sends a simple message back to the client

def handle_client(client_socket): 
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Recieved: {request.decode("utf-8")}')
        sock.send(b'ACK')

    if __name__ == '__main__':
        main()
