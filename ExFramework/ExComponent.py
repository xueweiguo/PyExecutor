from tkinter import * # get widget classes

class ExComponent:
    def __init__(self, name, comment):
        self.__name = name
        self.__comment__ = comment
        self.__tag = None
        self.canvas = None
        self.frame = None
        self.children = []
        #print(self)

    def set_tag(self, tag):
        self.__tag = tag
        for c in self.children:
            c.set_tag(tag)

    def tag(self):
        return self.__tag

    def name(self):
        return self.__name

    def comment(self):
        return self.__comment__

    def attach(self, canvas):
        self.canvas = canvas

    def countChild(self, child_class):
        count = 0
        for child in self.children:
            if isinstance(child, child_class):
                count = count + 1
        return count

    def findChild(self, name):
        for child in self.children:
            if child.name() == name:
                return child
        return None

    def serialize(self):
        return {'type':str(type(self)), 'tag':self.tag(), 'name':self.name}




