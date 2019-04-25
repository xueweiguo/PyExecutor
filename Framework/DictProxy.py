from Framework.ComponentDict import *

class DictProxy(object):
    _instance = None

    def __new__(cls):
        if not DictProxy._instance:
            cls._instance = super(DictProxy, cls).__new__(cls)
            cls._instance.__dict = None
        return DictProxy._instance

    def __init__(self):
        pass

    def register(self, component):
        self.__dict.register(component)

    def unregister(self, component):
        self.__dict.unrigister(component)

    def clear(self):
        if self.__dict:
            self.__dict.clear()

    def new(self):
        self.__dict = ComponentDict()
        self.__dict.new()

    def save(self, fn):
        return self.__dict.save(fn)

    def load(self, fn):
        return self.__dict.load(fn)

    def component(self, tag):
        return self.__dict.component(tag)









