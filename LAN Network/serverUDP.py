import socket
import time

# take the server name and port name
broadcast_IP = '255.255.255.255'
port = 5000

# create a socket at server side
s = socket.socket(socket.AF_INET, 
				socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# send to broadcast destination IP

message = "Broadcast message!"
while 1:
    s.sendto(message.encode(), (broadcast_IP, port))
    time.sleep(10)


# disconnect the server
s.close()
