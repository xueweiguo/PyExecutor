from tkinter import *
from Foundation.Observable import Observable


class ExecCanvas(Canvas):
    def __init__(self, master, *cnf, **kw):
        Canvas.__init__(self, master, *cnf, **kw)
        self.__uc = {}
        self.__observable = Observable()

    def clear_state(self):
        self.__uc.clear()

    def undo_controller(self, key):
        from Framework.DiagramUC import DiagramUC
        uc = self.__uc.get(key)
        if not uc:
            uc = DiagramUC(key)
            self.__uc[key] = uc
        return uc

    def modified(self):
        for am in self.__uc.values():
            if not am.undone(): #可以undo意味着有过修改。
                return True
        return False

    def observable(self):
        return self.__observable
