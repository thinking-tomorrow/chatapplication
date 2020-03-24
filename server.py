import socket
import database as db

server_socket = socket.socket()
server_socket.bind(('localhost', 1234))
server_socket.listen(5)


def get_user(username):
    return db.get_user(username)


def add_user(username, email, password):
    return db.add_user(username, email, password)


while True:
    client_socket, addr = server_socket.accept()
    print("Connected with ", addr)
    request = bytes.decode(client_socket.recv(1024), 'utf-8')

    if 'add_user' in request:
        x = request.split(',')
        client_socket.send(bytes(str(db.add_user(x[1], x[2], x[3])), 'utf-8'))
    elif 'get_user' in request:
        x = request.split(',')
        client_socket.send(bytes(str(db.get_user(x[1])), 'utf-8'))
    elif 'send_message' in request:
        x = request.split(',')
        client_socket.send(bytes(str(db.send_message(x[1], x[2], x[3]))))
