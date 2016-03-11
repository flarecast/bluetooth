import bluetooth
from threading import *
from message_handler import on_message

class ClientHandler(Thread):
    BUFFER_SIZE = 1024

    def __init__(self, sock, info):
        Thread.__init__(self)
        self.sock = sock
        self.info = info

    def run(self):
        # TODO: remove while true to handle client disconnect
        while True:
            data = sock.recv(BUFFER_SIZE)
            # TODO: try without threads, handle the request inside the handler
            Thread.__init__(ClientHandler.RequestHandler(data)).start()

    class RequestHandler(Thread):
        def __init__(self, data):
            # TODO: transform the data into a message
            self.data = data

        @on_message
        def run(self):
            # TODO: convert to message and return
            print("Just received" + self.data)
