from FunctionBlockDiagram.CommPort import *
class WifiPort(CommPort):
    def __init__(self, address):
        CommPort.__init__(self, address)

    def send_str(self, str):
        CommPort.send_str(self, str)

    def recv_str(self):
        return CommPort.recv_str(self)