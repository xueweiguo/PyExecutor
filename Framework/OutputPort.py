import copy
from Foundation.Iterators import *
from Framework.DataPort import *


# 信息标签
class OutputPort(DataPort):
    def __init__(self, parent=None, pos=0, name="", comment=""):
        DataPort.__init__(self, parent, pos, name, comment)
        self.x = None
        self.y = None
        self.__c_tags = []

    def copy(self, memo):
        c = DataPort.copy(self, memo)
        c.x = self.x
        c.y = self.y
        c.__c_tags = copy.copy(self.__c_tags)
        return c

    def reset_connections(self, memo):
        temp = self.__c_tags
        self.__c_tags = []
        for t in temp:
            new_tag = memo.get(t)
            if new_tag:
                self.__c_tags.append(new_tag)

    def accept(self, visitor, mode='DLR'):
        visitor.visit_output(self)

    def attach_canvas(self, canvas):
        self.calculate_position()
        canvas.create_rectangle(self.x, self.y - 3, self.x + 10, self.y + 3, fill='cyan',
                                             tags=[self.parent.tag, self.tag, self.frame])
        canvas.create_text(self.x - 2, self.y, tags=[self.parent.tag, self.tag, self.caption],
                           text=self.name, anchor=E)
        DataPort.attach_canvas(self, canvas)

    def point(self):
        bound_rect = self.canvas.coords(self.frame)
        pos = []
        pos.append(bound_rect[2])
        pos.append((bound_rect[1] + bound_rect[3])/2)
        return pos

    def connector(self, index):
        if (index >= 0) and (index < self.c_count()):
            return self.dict[self.__c_tags[index]]
        else:
            return None

    def data_source(self):
        from Framework.InputBlock import InputBlock
        from Framework.OutputBlock import OutputBlock
        from Framework.CustomBlock import CustomBlock
        if isinstance(self.parent, InputBlock):
            custom_block = self.get_ancestor(CustomBlock)
            for in_port in custom_block.iter('input_port'):
                if in_port.name == self.parent.name:
                    return in_port.data_source()
            return None
        elif isinstance(self.parent, CustomBlock):
            diagram = self.parent.diagram()
            for out_block in type_filter(diagram.iter(), OutputBlock):
                if out_block.name == self.name:
                    in_port = out_block.port('')
                    return in_port.data_source()
            return None
        else:
            return self

    def c_count(self):
        return len(self.__c_tags)

    def connector_iter(self):
        if self.dict:
            return map(self.dict.__getitem__, self.__c_tags)
        else:
            return iter([])

    def attach_connector(self, c):
        self.__c_tags.append(c.tag)
        self.handle_request(self, 'attach_connector', {'connector':c})

    def detach_connector(self, c):
        try:
            self.__c_tags.remove(c.tag)
        except:
            pass
        else:
            self.handle_request(self, 'detach_connector', {'connector':c})

    def on_move(self):
        for c in self.__c_tags:
            coords = self.point()
            self.dict[c].move_first(coords[0], coords[1])

    def calculate_position(self):
        block = self.parent
        self.x = block.right
        self.y = block.top + block.caption_height() + self.height() / 2
        self.y = self.y + self.pos * self.height()
        if block.last_pos < self.pos:
            block.last_pos = self.pos

    def relocation(self):
        self.calculate_position()
        self.canvas.coords(self.frame, self.x, self.y - 3, self.x + 10, self.y + 3)
        self.canvas.coords(self.caption, self.x - 2, self.y)
        self.on_move()

    def connected(self):
        return len(self.__c_tags) > 0