from Foundation.Iterators import *
from Framework.DataPort import *


#输入端口
class InputPort(DataPort):
    def __init__(self, parent=None, pos = 0, name="", comment="", color='black'):
        DataPort.__init__(self, parent, pos, name, comment)
        self.__connector = None
        self.color = color

    def copy(self, memo):
        c = DataPort.copy(self, memo)
        c.__connector = self.__connector
        return c

    def reset_connections(self, memo):
        if self.connected():
            self.__connector = memo.get(self.__connector)

    def accept(self, visitor, mode='DLR'):
        visitor.visit_input(self)

    @property
    def connector(self):
        if self.__connector:
            return self.dict[self.__connector]
        else:
            return None

    def data_source(self):
        if self.connector:
            return self.connector.output().data_source()
        else:
            return self

    def attach_canvas(self, canvas):
        self.calculate_position()
        canvas.create_rectangle(self.x - 10, self.y - 3, self.x, self.y + 3, fill='cyan',
                               tags=[self.parent.tag, self.tag, self.frame])
        canvas.create_text(self.x + 2, self.y, tags=[self.parent.tag, self.tag, self.caption],
                           text=self.name, anchor=W, fill=self.color)
        DataPort.attach_canvas(self, canvas)

    def point(self):
        bound_rect = self.canvas.coords(self.frame)
        pos = []
        pos.append(bound_rect[0])
        pos.append((bound_rect[1] + bound_rect[3])/2)
        return pos

    def set_connector(self, c):
        self.handle_request(self, 'set_connector', {'prev': self.connector, 'new': c})
        if c:
            self.__connector = c.tag
        else:
            self.__connector = None
        #print(self.connector)

    def on_move(self):
        if self.connector:
            coords = self.point()
            self.connector.move_last(coords[0], coords[1])

    def calculate_position(self):
        block = self.parent
        self.x = block.left
        self.y = block.top + block.caption_height() + self.height() / 2
        self.y = self.y + self.pos * self.height()
        if block.last_pos < self.pos:
            block.last_pos = self.pos

    def relocation(self):
        self.calculate_position()
        self.canvas.coords(self.frame, self.x - 10, self.y - 3, self.x, self.y + 3)
        self.canvas.coords(self.caption, self.x + 2, self.y)
        self.on_move()

    def connected(self):
        return self.connector is not None
