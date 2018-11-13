from tkinter import * # get widget classes

class ExComponent:
    def __init__(self, name):
        self.name = name
        self.tag = None
        self.canvas = None
        self.frame = None
        self.children = []
        print(self)

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
            if child.name==name:
                return child
        return None

    def serialize(self):
        return {'type':str(type(self)), 'tag':self.tag, 'name':self.name}



