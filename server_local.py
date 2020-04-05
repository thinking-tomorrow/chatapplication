import socket
import ast

# receiver_socket = socket.socket()
# receiver_socket.connect(('localhost', 1234))

HEADER_SIZE = 10


def send(msg):
    client_socket = socket.socket()
    client_socket.connect(('localhost', 1234))
    client_socket.send(bytes(f"{len(msg):<{HEADER_SIZE}}" + msg, 'utf-8'))
    data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    client_socket.close()
    return data


def get_user(username):
    return send(f"get_user,{username}")


def get_contact(details):
    return send(f"get_contact,{details}")


def add_user(username, email, password):
    return send(f"add_user,{username},{email},{password}")


def send_message(message, contact, now, sender):
    return send(f"send_message,{message},{contact},{now},{sender}")


def change_password(username, password):
    return send(f"change_password,{username},{password}")


def change_status(username, new_status):
    return send(f"change_status,{username},{new_status}")


def change_image(username, imagepath):
    pass
    # img = open(imagepath, 'rb')
    # client_socket = socket.socket()
    # client_socket.connect(('localhost', 1234))
    # client_socket.send(bytes(f"change,{username},{password}", 'utf-8'))
    # data = ast.literal_eval(bytes.decode(client_socket.recv(1024), 'utf-8'))
    # client_socket.close()
    # return data
