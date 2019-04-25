import sys
from FunctionBlock.WifiPort import *
from FunctionBlock.BluetoothPort import *


class CommPortFactory:
    def __init__(self):
        pass

    #取得WIFI端口
    def get_wifi(self, address):
        wifi = WifiPort(address)
        return wifi

    #取得蓝牙端口
    def get_bluetooth(self, address):
        bt = BluetoothPort(address)
        return bt

