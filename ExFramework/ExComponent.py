from tkinter import * # get widget classes

class ExComponent:
    def __init__(self, parent, name, comment):
        self.__parent = parent
        self.__tag = None
        self.__name = name
        self.__comment= comment
        self.__tag = None
        self._canvas = None
        self._frame = None

    def construct(self):
        return self

    @property
    def parent(self):
        return self.__parent

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def comment(self):
        return self.__comment

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, canvas):
        if canvas:
            self.attach_canvas(canvas)
        else:
            self.detach_canvas()

    #@canvas.setter
    def attach_canvas(self, canvas):
        self._canvas = canvas

    def detach_canvas(self):
        self._canvas.delete(self._frame)
        self._frame = None
        self._canvas = None

    def serialize(self):
        return {'type':str(type(self)), 'tag':self.tag, 'name':self.name}

    def handle_request(self, component, req, params=None):
        if self.__parent:
            return self.__parent.handle_request(component, req, params)
        else:
            return None




