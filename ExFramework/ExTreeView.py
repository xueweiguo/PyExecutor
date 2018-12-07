from tkinter import *
from tkinter.ttk import *

class ExTreeView(Frame):
    def __init__(self, parent, side):
        Frame.__init__(self, parent, relief=GROOVE)
        self.pack(side=side, fill=Y, ipadx=2, ipady=2)
        self.tree = Treeview(self)
        self.tree.heading('#0', text='BlockTree', anchor='w')
        myid = self.tree.insert("", 0, "中国", text="中国China", values=("1"))  # ""表示父节点是根
        myidx1 = self.tree.insert(myid, 0,"广东",text="中国广东",values=("2"))  # text表示显示出的文本，values是隐藏的值
        myidx2 = self.tree.insert(myid,1,"江苏",text="中国江苏",values=("3"))
        myidy = self.tree.insert("",1,"美国",text="美国USA",values=("4"))
        myidy1= self.tree.insert(myidy,0,"加州",text="美国加州",values=("5"))
        self.tree.pack()

    def update(self):
        pass
