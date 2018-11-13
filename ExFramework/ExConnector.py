from ExFramework.ExComponents import *
from ExFramework.ExOutputPort import *
from ExFramework.ExInputPort import *
from ExFramework.ExTagFactory import *

#连接线
class ExConnector(ExComponent):
    def __init__(self, name):
        ExComponent.__init__(self, name)
        self.tag = ExTagFactory().createTag()
        self.outputport = None
        self.inputport = None
        self.line = None

    def attach(self, canvas):
        ExComponent.attach(self, canvas)

    def setOutputPort(self, port):
        if isinstance(port, ExOutputPort)==False:
            return False
        coords = port.connectPoint()
        self.startLine(coords[0] , coords[1])
        self.outputport = port

    def setInputPort(self, port):
        if isinstance(port, ExInputPort)==False:
            return False
        coords = port.connectPoint()
        self.moveLastPoint(coords[0], coords[1])
        self.inputport = port

    def startLine(self, x, y):
        self.line = self.canvas.create_line(x, y, x, y, tag=self.tag, arrow=LAST)

    def moveLastPoint(self, x, y):
        if self.line:
            coords = self.canvas.coords(self.line)
            last_index = int(len(coords) / 2) - 1
            if last_index % 2 != 0:
                coords[last_index * 2] = x
            else:
                coords[last_index * 2 + 1] = y
            self.canvas.coords(self.line, coords)

    def removeLastPoint(self):
        if self.line:
            coords = self.canvas.coords(self.line)
            length = len(coords)
            if length > 2:
                coords.pop()
                coords.pop()
                print(coords)
                if len(coords) >= 4:
                    self.canvas.coords(self.line, coords)
                else:
                    self.canvas.delete(self.line)
                    self.line = None

    def appendPoint(self):
        if self.line:
            coords = self.canvas.coords(self.line)
            data_count = len(coords)
            coords.append(coords[data_count - 2])
            coords.append(coords[data_count - 1])
            self.canvas.coords(self.line, coords)

    def serialize(self):
        dict = ExComponent.serialize(self)
        dict['coords'] = self.canvas.coords(self.line)
        return dict
