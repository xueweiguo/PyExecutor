import sys
from FunctionBlockDiagram.WifiPort import *
from FunctionBlockDiagram.BluetoothPort import *

class CommPortFactory:
    def __init__(self):
        self.wifis = dict()
        self.bluetooths = dict()

    def get_wifi(self, address):
        wifi = self.wifis.get(address)
        if wifi:
            return wifi
        wifi = WifiPort(address)
        self.wifis[address] = wifi
        return wifi

    def get_bluetooth(self, address):
        bt = self.bluetooths.get(address)
        if bt:
            return bt
        bt = BluetoothPort(address)
        self.bluetooths[address] = bt
        return bt

    def release_idle(self):
        for key in self.wifis.keys():
            # getrefcount和self.wifis各引起引用计数+1
            if sys.getrefcount(self.wifis[key]) == 2:
                print('Deleteing port',self.wifis[key])
                self.wifis.pop(key)
                break
        for key in self.bluetooths.keys():
            # getrefcount和self.bluetooths各引起引用计数+1
            if sys.getrefcount(self.bluetooths[key]) == 2:
                print('Deleteing port', self.bluetooths[key])
                self.bluetooths.pop(key)
                break


