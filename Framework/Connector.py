import copy
from Framework.Component import *
from Framework.OutputPort import *
from Framework.InputPort import *


#连接线
class Connector(Component):
    def __init__(self, parent=None, name=''):
        Component.__init__(self, parent, name, '')
        self.__out_tag = None
        self.__in_tag = None
        self.active = None
        self.coords = None

    def copy(self, memo):
        c = Component.copy(self, memo)
        c.active = None
        c.coords = copy.copy(self.coords)
        return c

    def reset_connections(self, memo):
        self.__out_tag = memo.get(self.__out_tag)
        self.__in_tag = memo.get(self.__in_tag)

    def drag_begin(self):
        self.handle_request(self, 'drag_begin', {'coords': self.coords})

    def drag_end(self):
        self.handle_request(self, 'drag_end', {'coords':self.coords})

    def add_begin(self):
        self.handle_request(self, 'begin_macro')

    def add_end(self):
        self.handle_request(self, 'end_macro')

    def add_cancel(self):
        self.handle_request(self, 'cancel_macro')

    def attach_view(self, view):
        Component.attach_view(self, view)
        if self.coords:
            self.canvas.create_line(self.coords, tag=self.tag, arrow=LAST)

    def detach_view(self):
        try:
            self.canvas.delete(self.tag)
        except:
            pass
        else:
            Component.detach_view(self)

    def accept(self, visitor, mode='DLR'):
        visitor.visit_connector(self)

    def create_memento(self):
        return copy.copy(self.coords)

    def set_memento(self, memento):
        self.__set_coords(memento)

    def attach_output(self, port):
        if isinstance(port, OutputPort):
            self.__start(port.point()[0], port.point()[1])
            self.set_output(port)
            return True
        else:
            return False

    def set_output(self, port):
        if port:
            self.__out_tag = port.tag
            port.attach_connector(self)
        else:
            self.output().detach_connector(self)
            self.__out_tag = None

    def attach_input(self, port):
        if not isinstance(port, InputPort):
            return False
        # (self)
        pt = port.point()
        coords = self.canvas.coords(self.tag)
        pt_count = (int)(len(coords) / 2)
        # print('pt_count:', pt_count)
        if pt_count % 2 != 0:
            self.append_last()
        self.move_last(pt[0], pt[1])
        # self.__arrange_line()
        self.set_input(port)
        # print(self)

    def set_input(self, port):
        if port:
            self.__in_tag = port.tag
            port.set_connector(self)
        else:
            self.input().set_connector(None)
            self.__in_tag = None

    def disconnect(self):
        if self.output():
            self.handle_request(self, 'change_member',
                                {'setter': Connector.set_output, 'getter': Connector.output})
            self.set_output(None)

        if self.input():
            self.handle_request(self, 'change_member',
                                {'setter': Connector.set_input, 'getter': Connector.input})
            self.set_input(None)

    def move_first(self, pt_x, pt_y):
        try:
            coords = self.canvas.coords(self.tag)
        except:
            pass
        else:
            if len(coords) <= 4:
                x = int((coords[0] + coords[2]) / 2)
                y = int((coords[1] + coords[3]) / 2)
                coords.insert(2, y)
                coords.insert(2, x)
                coords.insert(2, y)
                coords.insert(2, x)
            coords[0] = pt_x
            coords[1] = pt_y
            coords[3] = pt_y
            self.__set_coords(coords)

    def drag_last(self, x, y):
        try:
            coords = self.canvas.coords(self.tag)
        except:
            pass
        else:
            pt_count = (int)(len(coords) / 2)
            index = pt_count - 1
            if  index % 2 != 0:
                coords[index * 2] = x
            else:
                coords[index * 2 + 1] = y
            self.__set_coords(coords)
            # print('drag_last')
            # print(self)

    def remove_last(self):
        try:
            coords = self.canvas.coords(self.tag)
        except:
            pass
        else:
            pt_count = (int)(len(coords) / 2)
            if pt_count > 2:
                coords.pop()
                coords.pop()
                self.__set_coords(coords)
            else:
                self.__set_coords(None)

    def append_last(self):
        # print('append_last')
        try:
            coords = self.canvas.coords(self.tag)
        except:
            pass
        else:
            data_count = len(coords)
            coords.append(coords[data_count - 2])
            coords.append(coords[data_count - 1])
            self.__set_coords(coords)

    def set_color(self, c):
        self.canvas.itemconfigure(self.tag, fill=c)

    def select_segment(self, x, y):
        self.active = None
        coords = self.canvas.coords(self.tag)
        #最初段，最后段禁止拖动
        i = 2
        while i < (len(coords) - 4):
            if i % 4 == 0:
                if abs(y - coords[i + 1]) <= 2:
                    if(x >= coords[i]) and (x <= coords[i + 2]):
                        self.active = int(i / 2)
                        break
                    elif (x <= coords[i]) and (x >= coords[i + 2]):
                        self.active = int(i / 2)
                        break
            else:
                if abs(x - coords[i]) <= 2:
                    if (y >= coords[i + 1]) and (y <= coords[i + 3]):
                        self.active = int(i / 2)
                        break
                    if (y <= coords[i + 1]) and (y >= coords[i + 3]):
                        self.active = int(i / 2)
                        break
            i = i + 2
        # print('self.active=', self.active)

    def move(self, cx, cy):
        if self.active:
            coord = self.canvas.coords(self.tag)
            if self.active % 2:
                coord[self.active * 2] = coord[self.active * 2] + cx
                coord[self.active * 2 + 2] = coord[self.active * 2 + 2] + cx
            else:
                coord[self.active * 2 + 1] = coord[self.active * 2 + 1] + cy
                coord[self.active * 2 + 3] = coord[self.active * 2 + 3] + cy
            self.__set_coords(coord)

    def create_popup(self, handler):
        menu = Menu(self.canvas, tearoff=False)
        menu.add_command(label='Delete', command=(lambda: handler.on_command('Delete')))
        return menu

    def input(self):
        if self.__in_tag:
            return self.dict[self.__in_tag]
        else:
            return None

    def output(self):
        if self.__out_tag:
            return self.dict[self.__out_tag]
        else:
            return None

    def __arrange_line(self):
        pass
        try:
            coord = self.canvas.coords(self.tag)
        except:
            pass
        else:
            while True:
                pt_count = int(len(coord) / 2)
                for index in range(0, pt_count - 2):
                    xi = index * 2
                    yi = xi + 1
                    if (coord[xi] == coord[xi + 2] and coord[xi + 2] == coord[xi + 4]) or (coord[yi] == coord[yi + 2] and coord[yi + 2] == coord[yi + 4]):
                        coord.pop(yi + 2)
                        coord.pop(xi + 2)
                if pt_count == int(len(coord) / 2):
                    break

            self.__set_coords(coord)
            #print('arranged:', coords)

    def __set_coords(self, coords):
        if coords:
            self.canvas.coords(self.tag, coords)
        else:
            self.canvas.delete(self.tag)
        self.coords = coords
        self.handle_request(self, 'connector_coords_changed')

    def move_last(self, port_x, port_y):
        try:
            coords = self.canvas.coords(self.tag)
        except:
            pass
        else:
            if len(coords) <= 4:
                x = int((coords[0] + coords[2]) / 2)
                y = int((coords[1] + coords[3]) / 2)
                coords.insert(2, y)
                coords.insert(2, x)
                coords.insert(2, y)
                coords.insert(2, x)

            last_index = len(coords) - 1
            coords[last_index - 1] = port_x
            coords[last_index] =  port_y
            coords[last_index - 2] = port_y
            self.__set_coords(coords)

    @property
    def x(self):
        return self.coords[0]

    def __start(self, x, y):
        self.canvas.create_line(x, y, x, y, tag=self.tag, arrow=LAST)
        self.coords = self.canvas.coords(self.tag)

    def __str__(self):
        coords = self.canvas.coords(self.tag)
        pt_count = (int)(len(coords)/2)
        ret = 'Tag:{},Pts:{},'.format(self.tag, pt_count)
        for pi in range(0, pt_count):
            ret += '({},{}),'.format(coords[pi * 2], coords[pi * 2 + 1])
        return ret


