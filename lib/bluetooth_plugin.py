from connection_plugin import ConnectionPlugin
from listener import Listener
from network_scanner import NetworkScanner

class BluetoothPlugin(ConnectionPlugin):
    def __init__(self):
        super().__init__()
        self.listener = Listener()

    # API method
    def broadcast(self, msg):
        print("BROADCASTING")
        NetworkScanner(msg).start()

    # API method
    def run(self):
        self.listener.start()

    # API method
    def address(self):
        # TODO: return bluetooth address
        return "12345"
