from connection_plugin import ConnectionPlugin
from listener import Listener
from network_scanner import NetworkScanner
import time
import thread

class BluetoothPlugin(ConnectionPlugin):

    def __init__(self):
        super().__init__()
        self.listener = Listener()
        self.addr = self.__get_bluetooth_addr()
        self.sent_message_ids = []
        self.last_removal = time.time()


    # API method
    def broadcast(self, msg):

        #Periodic message id removal
        if(time.time() > self.last_removal+1800):
            self.last_removal = time.time()
            thread.start_new_thread(self.remove_old_message_ids)

        #Only sends if not repeated
        if((msg.full_id(), msg.timestamp+msg.lifetime) not in self.sent_message_ids):
            self.sent_message_ids.append((msg.full_id(), msg.timestamp + msg.lifetime))
            print("BROADCASTING")
            NetworkScanner(msg, self).start()

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

    def remove_old_message_ids(self):
        curr_time = time.time()
        for (msg_id, endtime) in self.sent_message_ids:
            if endtime < curr_time:
                self.sent_message_ids.remove((msg_id, endtime))

