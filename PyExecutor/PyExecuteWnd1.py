import sys
sys.path.append('..')
from tkinter import * # get widget classes
from tkinter.messagebox import * # get standard dialogs

from ExComponents.ExComponents import *

from FunctionBlockDiagram.FbdComponentFactory import *
from FunctionBlockDiagram.FbdStartPoint import *
from FunctionBlockDiagram.FbdEndPoint import *
from FunctionBlockDiagram.FbdConnector import *
from FunctionBlockDiagram.SinFun import *
from FunctionBlockDiagram.CosFun import *
from FunctionBlockDiagram.MathFun import *
from FunctionBlockDiagram.GraphFun import *

class PyExecuteWnd(Tk):
    #初始化
    def __init__(self, title, parent = None):
        Tk.__init__(self, parent)
        self.title(title)
        self.makemenu()
        self.make_widgets()
    
    #准备画面组件
    def make_widgets(self):
        msg = Label(self, text='Add component from Add menu.') # add something below
        msg.pack(expand=YES, fill=BOTH)
        msg.config(relief=SUNKEN, width=40, height=7, bg='beige')

    #构建初始点
    def addInitial(self):
        self.current=FbdStartPoint('Initial');

    #构建终止点
    def addFinal(self):
        self.current=FbdEndPoint('Final');
                   
    #构建连接线
    def addConnector(self):
        self.current=FbdConnector();

    #构建功能块
    def addElement(self, name):
        if name == "Sin":
            self.current=SinFun(name)
        elif name == 'Cos':
            self.current=CosFun(name)
        elif name == 'Math':
            self.current=MathFun(name)
        elif name == "Graph":
            self.current=GraphFun(name)

    #构建信息标签
    def addNote(self):
        self.current=ExNote();

    #构建菜单 
    def makemenu(self):
        top = Menu(self)
        self.config(menu=top) # set its menu option

        file = Menu(top, tearoff=False)
        file.add_command(label='Quit', command=self.quit)
        top.add_cascade(label='File', menu=file)

        #添加图形要素菜单
        add = Menu(top, tearoff=False)
        add.add_command(label='Initial', command=(lambda:self.addInitial()))
        add.add_command(label='Final', command=(lambda:self.addFinal()))
        add.add_command(label='Connector', command=(lambda:self.addConnector()))
        
        #功能块子菜单
        submenu = Menu(add, tearoff = False)
        submenu.add_command(label="Sin", command=(lambda:self.addElement('Sin')))
        submenu.add_command(label="Cos", command=(lambda:self.addElement('Cos')))
        submenu.add_command(label="Math", command=(lambda:self.addElement('Math')))
        submenu.add_command(label="Graph", command=(lambda:self.addElement('Graph')))
        add.add_cascade(label='Elements', menu=submenu, underline=1)
        top.add_cascade(label='Add', menu=add)
        
        #添加标签菜单
        add.add_command(label='Note', command=(lambda:self.addNote()))


