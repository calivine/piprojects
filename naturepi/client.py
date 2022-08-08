import socket


class ClientHTTP:

    def __init__(self):
        self.client_socket = socket.socket()

    def start(self, addr):
        self.client_socket.connect((addr, 8000))
        return self.client_socket.makefile('wb')

    def close(self):
        self.client_socket.close()

