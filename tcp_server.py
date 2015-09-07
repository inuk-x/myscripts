#!/usr/bin/env python

'''

a very simple TCP server that listens on any arbitrary port set on the command line, accepts data from
a client and acknowledges receipt.

'''

import socket
import sys
import threading

# usage error message
usage = (
"\nUsage: tcpserver.py server_port\n"
)

if len(sys.argv) < 1:
    print usage
    sys.exit(0)

# establish server IP and port variables
bind_ip = "0.0.0.0"
bind_port = int(sys.argv[1])

# create socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind IP address and port to variables
server.bind((bind_ip,bind_port))

# set maximum number of backlog connections
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

# define client-handling thread
def handle_client(client_socket):
    
    # print client data sent
    request = client_socket.recv(1024)
    print "[*] Received %s" % request
    
    # send acknowledgement
    client_socket.send("\n\rACK!\n\r")
    
    # close socket
    client_socket.close()
    
while True:
    
    client,addr = server.accept()
    
    print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])
    
    # spin up client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
    
