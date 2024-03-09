import socket
import sys

SERVER_HOST = '10.0.2.15'
SERVER_PORT = 54323
BACKLOG = 5
print('Welcome to TCP Chat Server')
serv_name = input('Enter your name: ')
serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_sock.bind((SERVER_HOST, SERVER_PORT))
serv_sock.listen(BACKLOG)
print('Waiting for a connection request ...')
cli_sock,cli_addr = serv_sock.accept()
print('Connected to: ', cli_sock.getpeername()[0])
serv_name = serv_name.encode('utf-8')
cli_sock.send(serv_name)
msg = cli_sock.recv(1024)
cli_name = msg.decode('utf-8')
print(cli_name, 'has joined')
while True:
    msg = cli_sock.recv(1024)
    print(cli_name, ':-> ', msg.decode('utf-8'))
    if msg.decode('utf-8') == 'bye':
        print('Received bye from client :', cli_sock.getpeername()[0])
        break
    message = input('Me:-> ')
    if message == 'bye':
        message = message.encode('utf-8')
        cli_sock.send(message)
        print('Bye from server')
        break
    else:
        message = message.encode('utf-8')
        cli_sock.send(message)
cli_sock.close()
print('Connection closed')
