import socket
import ast

# receiver_socket = socket.socket()
# receiver_socket.connect(('localhost', 1234))

HEADER_SIZE = 10


def get_user(username):
    client_socket = socket.socket()
    client_socket.connect(('localhost', 1234))
    client_socket.send(bytes(f"get_user,{username}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    client_socket.close()
    return data


def get_contact(details):
    client_socket = socket.socket()
    client_socket.connect(('localhost', 1234))
    client_socket.send(bytes(f"get_contact,{details}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    client_socket.close()
    return data


def add_user(username, email, password):
    client_socket = socket.socket()
    client_socket.connect(('localhost', 1234))
    client_socket.send(bytes(f"add_user,{username},{email},{password}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    client_socket.close()
    return data


def send_message(message, contact, now, sender):
    client_socket = socket.socket()
    client_socket.connect(('localhost', 1234))
    client_socket.send(bytes(f"send_message,{message},{contact},{now},{sender}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    client_socket.close()
    return data

def change_image(username,profileimage):
    for i in range(4):
        print(i)
        print('in server local')
    client_socket = socket.socket()
    client_socket.connect(('localhost',1234))
    print('H')
    client_socket.send(bytes(f"image_message,{username},{profileimage}", 'utf-8'))
    print('Hello!')
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024),'utf-8'))
    print('Hello!')
    client_socket.close()
    print('Hello!')
    return data
