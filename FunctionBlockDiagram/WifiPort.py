from FunctionBlockDiagram.CommPort import *
class WifiPort(CommPort):
    def __init__(self, address):
        CommPort.__init__(self, address)

    def send_data(self, data):
        CommPort.send_data(self, data)

    def recv_data(self):
        return CommPort.recv_data(self)