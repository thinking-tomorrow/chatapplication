import socket

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
server_socket.bind(('2401:4900:1109:70ad:155a:2db3:1b76:ad15', 1234))
server_socket.listen(5)
