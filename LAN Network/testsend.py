import socket

host = "172.16.202.14"
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port))
        s.sendall(b"Hello")
        data = s.recv(1024)
print(f"Recieved {data}")
