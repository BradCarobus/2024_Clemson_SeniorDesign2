import socket

# take the server name and port name

receive_IP = '0.0.0.0'
port = 5000

# create a socket at client side
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#bind socket
s.bind((receive_IP, port))

#receive and print messages from server, destinatin IP for broadcast is different than receiving IP
while True:
    data, addr = s.recvfrom(1024)
    print("Receive message from {}: {}".format(addr, data.decode()))

s.close()
