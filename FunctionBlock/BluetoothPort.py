from FunctionBlock.CommPort import *


class BluetoothPort(CommPort):
    def __init__(self, address):
        CommPort.__init__(self)
        self.address = address

    def open(self):
        pass

    def close(self):
        pass

    def send_data(self, str):
        CommPort.send_data(self, str)

    def recv_data(self):
        return CommPort.recv_data(self)