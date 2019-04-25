import abc


class TreeAccessor(metaclass=abc.ABCMeta):
    def __init__(self):
        self.__observer__ = None

    # 取得父节点
    @abc.abstractmethod
    def get_parent(self, node):
        pass

    # 取得下级节点
    @abc.abstractmethod
    def get_children(self, node):
        pass

    # 取得节点名称
    @abc.abstractmethod
    def get_name(self, node):
        pass

    # 取得节点iid
    def get_iid(self, node):
        return None

    # 取得节点图标
    def get_image(self, node):
        return None

    #聚焦节点
    def focus(self, iid):
        pass


