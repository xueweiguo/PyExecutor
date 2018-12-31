class ExTreeAccessor:
    def __init__(self):
        self.__observer__ = None

    #取得根节点
    def get_root(self):
        pass

    #取得父节点
    def get_parent(self, node):
        pass

    #取得下级节点
    def get_children(self, node):
        pass
    #取得节点名称
    def get_name(self, node):
        pass

    # 取得节点iid
    def get_iid(self, node):
        pass

    # 取得节点图标
    def get_image(self, node):
        pass

    #聚焦节点
    def focus(self, iid):
        pass


