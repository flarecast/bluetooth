from connection_plugin import ConnectionPlugin
from listener import Listener
from network_scanner import NetworkScanner

class BluetoothPlugin(ConnectionPlugin):
    def __init__(self):
        super().__init__()
        self.listener = Listener()
        self.addr = self.__get_bluetooth_addr()

    # API method
    def broadcast(self, msg):
        print("BROADCASTING")
        NetworkScanner(msg).start()

    # API method
    def run(self):
        self.listener.start()

    # API method
    def address(self):
        return self.addr

    def __get_bluetooth_addr(self):
        with open('config/bluetooth_address', 'r') as file:
            addr = file.read()
        print(addr)
        return addr
