import socket
import database as db

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 1234))
server_socket.listen(5)

HEADER_SIZE = 10


def get_user(username):
    return db.get_user(username)


def add_user(username, email, password):
    return db.add_user(username, email, password)


while True:
    client_socket, addr = server_socket.accept()
    print("Connected with ", addr)

    request = bytes.decode(client_socket.recv(4096), 'utf-8')

    if 'add_user' in request:
        x = request.split(',')
        client_socket.send(bytes(str(db.add_user(x[1], x[2], x[3])), 'utf-8'))
    elif 'image_message' in request:
        print('hello')
        for i in range(4):
            print(i)
            print('in server')
        x = request.split(',')
        client_socket.send(bytes(db.uploadprofilepicture(str(x[1]),x[2])), 'utf-8')
    elif 'get_user' in request:
        x = request.split(',')
        client_socket.send(bytes(str(db.get_user(x[1])), 'utf-8'))
    elif 'send_message' in request:
        x = request.split(',')
        client_socket.send(bytes(str(db.send_message(x[1], x[2], x[3], x[4])), 'utf-8'))
    elif 'get_contact' in request:
        x = request.split(',')
        client_socket.send(bytes(str(db.get_contact(x[1])), 'utf-8'))

