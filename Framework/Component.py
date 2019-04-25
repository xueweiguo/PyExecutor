import copy
from tkinter import * # get widget classes
from Foundation.Iterators import *
from Framework.DictProxy import *


class Component(object):
    def __init__(self, cd, name, comment):
        self.__parent = None
        self.__tag = None
        self.__name = name
        self.__comment = comment
        self._dict = cd
        self._frame = None
        self.canvas = None

    def construct(self, parent):
        self.set_parent(parent)
        self.tag = self.dict.create_tag()
        self.dict.register(self)
        return self

    def destruct(self):
        self.dict.unregister(self)

    # 克隆接口
    def clone(self):
        from Framework.ConnectionCoordinator import ConnectionCoordinator
        memo = {}
        c = self.copy(memo)
        c.accept(ConnectionCoordinator(memo))
        return c

    # 具体复制处理
    def copy(self, memo):
        c = copy.copy(self)
        c.__parent = None
        c._frame = None
        c.canvas = None
        c.tag = self.dict.create_tag()
        self.dict.register(c)
        memo[self.tag] = c.tag
        return c

    def set_parent(self, parent):
        if parent:
            self.__parent = parent.tag
        else:
            self.__parent = None

    def iter(self, mode=''):
        return iter([])

    def accept(self, visitor, mode='DLR'):
        pass

    @property
    def dict(self):
        return self._dict

    def set_dict(self, dict):
        self._dict = dict

    @property
    def parent(self):
        if self.__parent:
            return self.dict[self.__parent]
        else:
            return None

    def get_ancestor(self, cls):
        parent = self.parent
        while parent:
            if isinstance(parent, cls):
                return parent
            parent = parent.parent
        return None

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def name(self):
        return self.get_name()

    @name.setter
    def name(self, name):
        self.set_name(name)

    @property
    def comment(self):
        return self.get_comment()

    @comment.setter
    def comment(self, comment):
        self.set_comment(comment)

    #@canvas.setter
    def attach_canvas(self, canvas):
        self.canvas = canvas

    def detach_canvas(self):
        self.canvas = None

    def find_child(self, tag):
        return None

    # 生成属性对话框
    def create_property_dlg(self):
        pass

    # 生成弹出菜单
    def create_popup(self, handler):
        pass

    def set_name(self, name):
        self.handle_request(self, 'change_member',
                            {'getter': Component.get_name,
                             'setter': Component.set_name})
        self.__name = name
        self.name_changed()

    def name_changed(self):
        pass

    def get_name(self):
        return self.__name

    def get_comment(self):
        return self.__comment

    def set_comment(self, comment):
        self.handle_request(self, 'change_member',
                            {'getter': Component.get_comment,
                             'setter': Component.set_comment})
        self.__comment = comment
        self.comment_changed()

    def comment_changed(self):
        pass

    #请求处理
    def handle_request(self, component, req, params=None):
        if self.parent:
            return self.parent.handle_request(component, req, params)
        else:
            return None

    def start(self, context):
        pass

    def stop(self, context):
        pass




