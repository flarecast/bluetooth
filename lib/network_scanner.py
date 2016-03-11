from threading import Thread
import bluetooth
import time

class NetworkScanner(Thread):
    def __init__(self, msg):
        Thread.__init__(self)
        self.emitted_devices = []
        self.insistence = msg.insistence
        self.msg = msg

    def broadcast(self):
        nearby_devices = scan_network
        for addr in nearby_devices:
            if addr not in self.emmitted_devices:
                emit(self.msg, addr)
                self.emitted_devices.insert(addr)

    def emit(msg, addr):
        NetworkScanner.Emitter(msg, addr).start();

    def scan_network(self):
        return bluetooth.discover_devices(lookup_names=False)

    def run(self):
        start = time.time()
        while start + self.insistence < time.time():
            self.broadcast()

    class Emitter(Thread):
        def __init__(self, msg, addr)
            Thread.__init__(self)
            self.msg = msg
            self.addr = addr
            self.sock = bluetooth.BluetoothSocket(RFCOMM)

        def run(self):
            sock.connect((self.addr, Server.DEFAULT_PORT))
            sock.send(self.msg)
            sock.close()

