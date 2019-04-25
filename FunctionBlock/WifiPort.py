from FunctionBlock.CommPort import *


class WifiPort(CommPort):
    def __init__(self, address=None):
        CommPort.__init__(self)
        self.address = address

    # 打开Wifi通信端口
    def open(self):
        return True

    # 关闭通信端口
    def close(self):
        return True

    def send_data(self, str):
        CommPort.send_data(self, str)

    def recv_data(self):
        return CommPort.recv_data(self)
