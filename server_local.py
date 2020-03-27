import socket
import ast

client_socket = socket.socket()
client_socket.connect(('localhost', 1234))

HEADER_SIZE = 10


def get_user(username):
    client_socket.send(bytes(f"get_user,{username}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024)))
    return data


def get_contact(details):
    client_socket.send(bytes(f"get_contact,{details}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    return data


def add_user(username, email, password):
    client_socket.send(bytes(f"add_user,{username},{email},{password}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    return data


def send_message(message, contact, now):
    client_socket.send(bytes(f"send_message,{message},{contact},{now}", 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    return data
