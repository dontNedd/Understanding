#TCP client
import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.conect((target_host,target_port))

#send some data
client.send = client.recv(4096)

#send some data
client.send(b"GET / HTTP/1.1\nHsot: google.com\r\n\r\n")

#receive some data
Response = client.recv(4096)

print(Response.decode())
client.close()


#UDP client #######################################
import socket 

target_host = "127.0.0.1"
target_port = 9997

#creat a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data
client.sendto(b"AABBBCCC",(target_host,target_port))

#receive some data
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()


#TCP Server ########################################
import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

if__name__ == '__main__':

main()


#Bunk Netcat
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

class NETCAT:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()
    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('> ')
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print('User terminated.')
            self.socket.close()
            sys.exit()

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
    return output.decode()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent('''Example:
        netcat.py -t 192.168.1.108 -p 5555 -l -c #command shell
        netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt #upload to file
        netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" #execute command
        echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
        netcat.py -t 192.168.1.108 -p 5555 # connect to server

    '''))
parser.add_argument('-c', '--command', action='store_true', help='command shell')
parser.add_argument('-c', '--execute', help='execute specified command')
parser.add_argument('-c', '--listen', action='store_true', help='listen')
parser.add_argument('-c', '--port', type=int, default=5555, help='specified port')
parser.add_argument('-c', '--target', default='192.168.1.203' , help='specified IP')
parser.add_argument('-c', '--upload', help='upload file')
args = parser.parse_args()
if args.listen:
    buffer = ''
else:
    buffer = sys.stdin.read()

nc = NETCAT(args, buffer.encode())
nc.run()


######################### idk where this goes in the main -bunk Netcat
def listen(self):
    self.socket.bind((self.args.target, self.args.port))
    self.socket.listen(5)
    while True:
        client_socket, _=self.socket.accept()
        slient_thread = threading.Thread(
            target=self.handle, args=(client_socket,)
        )
    client_thread.start()
        