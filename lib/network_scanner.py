from threading import Thread
from listener import Listener
from message import Message
import bluetooth
import time
import pickle

class NetworkScanner(Thread):
    device_blacklist = set()

    def __init__(self, msg):
        Thread.__init__(self)
        self.emitted_devices = set()
        self.msg = msg

    def broadcast(self):
        network = NetworkScanner.network()
        repeated_devices = Message.addrs(self.msg.id)
        blacklist = NetworkScanner.device_blacklist
        devices = network - repeated_devices - blacklist

        for addr in devices:
            self.emit(self.msg, addr)
            Message.register(self.msg.id, {addr})

    def emit(self, msg, addr):
        NetworkScanner.Emitter(msg, addr).start();

    @staticmethod
    def scan_network():
        return set(bluetooth.discover_devices(lookup_names=False))

    def run(self):
        start = time.time()
        self.emitted_devices.add(self.msg.sender)
        while start + self.msg.insistence > time.time():
            self.broadcast()

    class Emitter(Thread):
        def __init__(self, msg, addr):
            Thread.__init__(self)
            self.msg = msg
            self.addr = addr
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        def run(self):
            try:
                self.sock.connect((self.addr, Listener.DEFAULT_PORT))
                print("SENDING: "+self.addr)
                self.sock.send(pickle.dumps(self.msg))
                self.sock.close()
                Message.register(self.msg.id, {self.msg.sender})
            except Exception as e:
                self.sock.close()
                if(str(e) == "52"):
                    NetworkScanner.device_blacklist.add(self.addr)
                print(self.addr + " :: " + str(e))
                print("IGNORED DEVICE: "+self.addr)
