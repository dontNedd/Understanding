#TCP client
import socket

target_host = "www.google.com"
target_port = 80

#1create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2connect the client
client.conect((target_host,target_port))

#3send some data
client.send = client.recv(4096)

#4send some data
client.send(b"GET / HTTP/1.1\nHsot: google.com\r\n\r\n")

#5receive some data
Response = client.recv(4096)

print(Response.decode())
client.close()
