from tkinter import * # get widget classes

class ExComponent:
    def __init__(self, name, comment):
        self.__parent__ = None
        self.__name = name
        self.__comment__ = comment
        self.__tag = None
        self.canvas = None
        self.frame = None
        self.__children__ = []

    def set_parent(self, parent):
        self.__parent__ = parent

    def parent(self):
        return self.__parent__

    def set_tag(self, tag):
        self.__tag = tag
        for c in self.children():
            c.set_tag(tag)

    def tag(self):
        return self.__tag

    def name(self):
        return self.__name

    def comment(self):
        return self.__comment__

    def attach_canvas(self, canvas):
        self.canvas = canvas
        for c in self.children():
            c.attach_canvas(canvas)

    def detach_canvas(self):
        self.canvas.delete(self.frame)
        self.frame = None
        for c in self.children():
            c.detach_canvas()
        self.canvas = None

    def countChild(self, child_class):
        count = 0
        for child in self.children():
            if isinstance(child, child_class):
                count = count + 1
        return count

    def findChild(self, name):
        for child in self.children():
            if child.name() == name:
                return child
        return None

    def append(self, child):
        child.set_parent(self)
        self.__children__.append(child)
        self.notify(child, 'append')

    def remove(self, child):
        self.notify(child, 'remove')
        self.__children__.remove(child)

    def children(self):
        return self.__children__

    def serialize(self):
        return {'type':str(type(self)), 'tag':self.tag(), 'name':self.name}

    def notify(self, component, ext):
        if self.__parent__:
            self.__parent__.notify(component, ext)




