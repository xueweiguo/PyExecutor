from ExFramework.ExElement import *
from ExFramework.ExOutputPort import *
from ExFramework.ExInputPort import *

#连接线
class ExConnector(ExElement):
    def __init__(self, parent, name):
        ExElement.__init__(self, parent, name, '')
        self.output = None
        self.input = None
        self.line = None
        self.active = None
        self.coords = None

    def construct(self):
        self.tag = self.handle_request(self, 'create_tag')
        return self

    def attach_canvas(self, canvas):
        ExElement.attach_canvas(self, canvas)
        if self.coords:
            self.line = self._canvas.create_line(self.coords, tag=self.tag, arrow=LAST)

    def detach_canvas(self):
            if self.line:
                self._canvas.delete(self.line)
                self.line = None
            ExElement.detach_canvas(self)

    def setOutputPort(self, port):
        if isinstance(port, ExOutputPort):
            self.coords = port.point()
            self.startLine(self.coords[0] , self.coords[1])
            self.output = port
            port.add_connector(self)
            return True
        else:
            return False

    def setInputPort(self, port):
        if not isinstance(port, ExInputPort):
            return False
        pt = port.point()
        self.move_last(pt[0], pt[1])
        self.input = port
        port.set_connector(self)

    def disconnect(self):
        if self.output:
            self.output.remove_connector(self)
            self.output = None
        if self.input:
            self.input.set_connector(None)
            self.input = None

    def startLine(self, x, y):
        self.line = self._canvas.create_line(x, y, x, y, tag=self.tag, arrow=LAST)

    def move_first(self, x, y):
        if self.line:
            coords = self._canvas.coords(self.line)
            if len(coords) <= 4:
                x = int((coords[0] + coords[2]) / 2)
                y = int((coords[1] + coords[3]) / 2)
                coords.insert(2, y)
                coords.insert(2, x)
                coords.insert(2, y)
                coords.insert(2, x)
            coords[0] = x
            coords[1] = y
            coords[3] = y
            self.coords = coords
            self._canvas.coords(self.line, self.coords)

    def move_last(self, x, y):
        if self.line:
            coords = self._canvas.coords(self.line)
            if len(coords) <= 4:
                x = int((coords[0] + coords[2]) / 2)
                y = int((coords[1] + coords[3]) / 2)
                coords.insert(2, y)
                coords.insert(2, x)
                coords.insert(2, y)
                coords.insert(2, x)

            last_index = len(coords) - 1
            coords[last_index - 1] = x
            coords[last_index] =  y
            coords[last_index - 2] = y
            self.coords = coords
            self._canvas.coords(self.line, self.coords)

    def drag_last(self, x, y):
        if self.line:
            coords = self._canvas.coords(self.line)
            last_index = int(len(coords) / 2) - 1
            if last_index % 2 != 0:
                coords[last_index * 2] = x
            else:
                coords[last_index * 2 + 1] = y
            self.coords = coords
            self._canvas.coords(self.line, self.coords)

    def remove_last(self):
        if self.line:
            coords = self._canvas.coords(self.line)
            length = len(coords)
            if length > 2:
                coords.pop()
                coords.pop()
                if len(coords) >= 4:
                    self.coords = coords
                    self._canvas.coords(self.line, self.coords)
                else:
                    self._canvas.delete(self.line)
                    self.coords = None
                    self.line = None

    def append_last(self):
        if self.line:
            coords = self._canvas.coords(self.line)
            data_count = len(coords)
            coords.append(coords[data_count - 2])
            coords.append(coords[data_count - 1])
            self.coords = coords
            self._canvas.coords(self.line, self.coords)

    def set_color(self, c):
        self._canvas.itemconfigure(self.line, fill=c)

    def select_segment(self, x, y):
        self.active = None
        coords = self._canvas.coords(self.line)
        #最初段，最后段禁止拖动
        i = 2
        while i < (len(coords) - 2):
            if i % 4 == 0:
                if y == coords[i + 1]:
                    if(x >= coords[i]) and (x <= coords[i + 2]):
                        self.active = int(i / 2)
                        break
                    elif (x <= coords[i]) and (x >= coords[i + 2]):
                        self.active = int(i / 2)
                        break
            else:
                if x == coords[i]:
                    if (y >= coords[i + 1]) and (y <= coords[i + 3]):
                        self.active = int(i / 2)
                        break
                    if (y <= coords[i + 1]) and (y >= coords[i + 3]):
                        self.active = int(i / 2)
                        break
            i = i + 2

    def move(self, cx, cy):
        if self.active:
            coords = self._canvas.coords(self.line)
            if self.active % 2:
                coords[self.active * 2] = coords[self.active * 2] + cx
                coords[self.active * 2 + 2] = coords[self.active * 2 + 2] + cx
            else:
                coords[self.active * 2 + 1] = coords[self.active * 2 + 1] + cy
                coords[self.active * 2 + 3] = coords[self.active * 2 + 3] + cy
            self.coords = coords
            self._canvas.coords(self.line, self.coords)

    def serialize(self):
        dict = ExComponent.serialize(self)
        dict['coords'] = self._canvas.coords(self.line)
        return dict

    def create_popup(self, handler):
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu
