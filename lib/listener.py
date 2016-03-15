import bluetooth
from threading import *
from message_handler import on_message
import pickle

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

    def run(self):
        self.listen()
        while True:
            self.handle(self.ssock.accept())

    @on_message
    def handle(self, data):
        return pickle.loads(data[0].recv(1024))

