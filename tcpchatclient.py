import socket
import sys

SERVER_HOST = 'yell.networkprog.my'
SERVER_PORT = 54323
print('Welcome to TCP Chat Client')
name = input('Enter your name: ')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_HOST, SERVER_PORT))
print('Connected to: ', sock.getpeername()[0])
msg = sock.recv(1024)
serv_name = msg.decode('utf-8')
print('Connected to user name:', serv_name)
name = name.encode('utf-8')
sock.send(name)
while True:
    message = input('Me:- ')
    if message == 'bye':
        message = message.encode('utf-8')
        sock.send(message)
        print('Bye from client')
        break
    else:
        message = message.encode('utf-8')
        sock.send(message)
    msg = sock.recv(1024)
    print(serv_name, ':-> ', msg.decode('utf-8'))
    if msg.decode('utf-8') == 'bye':
        print('Received bye from server :', sock.getpeername()[0])
        break
sock.close()
print('Connection closed')
