class ExTreeAccessor:
    def __init__(self):
        self.__observer__ = None

    def get_root(self):
        pass

    def get_parent(self, node):
        pass

    def get_children(self, node):
        pass

    def get_name(self, node):
        pass

    def get_iid(self, node):
        pass

    def focus(self, iid):
        pass

    def attach_observer(self, observer):
        self.__observer__ = observer

    def notify(self, invoker, ext):
        if self.__observer__:
            self.__observer__.update(invoker, ext)

