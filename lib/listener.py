import bluetooth
from threading import *
from client_handler import ClientHandler

class Listener(Thread):
    DEFAULT_PORT = 1
    BUFFER_SIZE = 1024

    def __init__(self):
        Thread.__init__(self)
        self.port = Listener.DEFAULT_PORT
        self.ssock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def listen(self):
        self.ssock.bind(("", self.port))
        self.ssock.listen(1)
        return self.ssock.accept()

    def run(self):
        while True:
            self.handle(self.listen())

    # @on_message
    def handle(self, data):
        # TODO: return a message
        print("Just received: " + data[0])

