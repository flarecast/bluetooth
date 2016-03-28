from threading import Thread
from listener import Listener
import bluetooth
import time
import pickle

class NetworkScanner(Thread):
    device_blacklist = []


    def __init__(self, msg):
        Thread.__init__(self)
        self.emitted_devices = []
        self.msg = msg

    def broadcast(self):
        nearby_devices = self.scan_network()
        for addr in nearby_devices:
            if addr not in self.emitted_devices and addr not in NetworkScanner.device_blacklist:
                self.emit(self.msg, addr)
                self.emitted_devices.append(addr)
            else:
                print("ALREADY SENT TO: "+addr)

    def emit(self,msg, addr):
        NetworkScanner.Emitter(msg, addr).start();

    def scan_network(self):
        return bluetooth.discover_devices(lookup_names=False)

    def run(self):
        start = time.time()
        self.emitted_devices.append(self.msg.sender)
        while start + self.msg.insistence >  time.time():
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
            except Exception as e:
                self.sock.close()
                NetworkScanner.device_blacklist.append(self.addr)
                print(self.addr + " :: " + str(e))
                print("IGNORED DEVICE: "+self.addr)


