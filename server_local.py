import socket
import ast
from PIL import Image

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


def change_password(username, password):
    client_socket = socket.socket()
    client_socket.connect(('localhost', 1234))
    client_socket.send(bytes(f"change,{username},{password}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    client_socket.close()
    return data


def change_image(username, imagepath):
    pass
    # img = open(imagepath, 'rb')
    # client_socket = socket.socket()
    # client_socket.connect(('localhost', 1234))
    # client_socket.send(bytes(f"change,{username},{password}", 'utf-8'))
    # data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    # client_socket.close()
    # return data
